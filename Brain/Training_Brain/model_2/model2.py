import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_speak.speak import speak

with open(r'/home/hacksmith010/Programming/Personal/Jarvis/data/intents.json') as file:
    data = json.load(file)
    
training_data = []
for intent in data.get('intents',[]):
    if 'patterns' in intent:
        for pattern in intent['patterns']:
            training_data.append((pattern,intent['tag']))
    else:
        print(f"Warning: 'patterns' key not found for intent: {intent}")
        
if not training_data:
    print("No training data found. Exiting.")
else:
    x,y = zip(*training_data)
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(x)
    classifier = MultinomialNB()
    classifier.fit(x,y)
    
    def get_response(user_input):
        user_input_vectorized = vectorizer.transform([user_input])
        
        predicted_intent = classifier.predict(user_input_vectorized)[0]
        
        for intent in data.get('intents',[]):
            if intent.get('tag') == predicted_intent:
                responses = intent.get('responses',[])
                if responses:
                    return random.choice(responses)
                else:
                    return "I'm sorry, I don't have a response for that."
        return "I'm sorry, I don't understand."
    