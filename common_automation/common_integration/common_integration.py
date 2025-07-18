import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from common_automation.common_open.open import *
from common_automation.common_close.close import *

def common_cmd(query):
    if "open" in query or "kholo" in query:
        query.replace("open", "")
        query.replace("kholo", "")
        open(query)
    elif "close" in query or "band kar do" in query:
        close()
    else:
        pass
        