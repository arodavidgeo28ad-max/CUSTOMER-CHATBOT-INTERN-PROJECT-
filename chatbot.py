import json
import random
import re

def load_intents():
    with open('intents.json', 'r') as file:
        return json.load(file)

def get_response(user_input):
    intents = load_intents()
    # Normalize input
    user_input = user_input.lower()
    user_input = re.sub(r'[^\w\s]', '', user_input)
    
    best_match = None
    max_score = 0
    
    for intent in intents['intents']:
        score = 0
        for pattern in intent['patterns']:
            if pattern.lower() in user_input:
                score += 1
        
        if score > max_score:
            max_score = score
            best_match = intent
            
    if best_match and max_score > 0:
        return random.choice(best_match['responses'])
    
    return "I'm not sure I understand. Could you please rephrase that or contact our support team?"
