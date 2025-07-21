import pyaudio
import struct
import math
import time
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
BLOCK_DURATION = 0.02 
BLOCK_SIZE = int(RATE * BLOCK_DURATION)

THRESHOLD = 0.4         
SUDDEN_SPIKE = 0.25
ZCR_THRESHOLD = 0.12
CLAP_GAP = 0.4
REQUIRED_CLAPS = 2

SHORT_NORMALIZE = (1.0 / 32768.0)

def get_rms(block):
    count = len(block) // 2
    format_string = f"{count}h"
    shorts = struct.unpack(format_string, block)
    sum_squares = sum((sample * SHORT_NORMALIZE) ** 2 for sample in shorts)
    return math.sqrt(sum_squares / count)

def get_zcr(block):
    count = len(block) // 2
    format_string = f"{count}h"
    shorts = np.array(struct.unpack(format_string, block))

    crossings = np.sum(np.sign(shorts[:-1]) != np.sign(shorts[1:]))
    return crossings / (count - 1)

def clap_detect():
    print("Listening for claps...")

    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       frames_per_buffer=BLOCK_SIZE)

    clap_count = 0
    last_clap_time = 0
    previous_amplitude = 0

    try:
        while True:
            block = stream.read(BLOCK_SIZE, exception_on_overflow=False)
            amplitude = get_rms(block)
            zcr = get_zcr(block)

            current_time = time.time()

            if (
                amplitude > THRESHOLD and
                zcr > ZCR_THRESHOLD and
                (amplitude - previous_amplitude) > SUDDEN_SPIKE and
                (current_time - last_clap_time) > CLAP_GAP
            ):
                clap_count += 1
                last_clap_time = current_time
                print(f"👏Clap #{clap_count} detected (Amp: {amplitude:.3f}, ZCR: {zcr:.3f})")

                if clap_count >= REQUIRED_CLAPS:
                    print("✅Clap sequence detected!")
                    break
            
            elif (current_time - last_clap_time) > 2.0 and clap_count > 0:
                 clap_count = 0 
                 
            previous_amplitude = amplitude
            time.sleep(0.005)

    except KeyboardInterrupt:
        print("Detection stopped by user.")
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
