import json
import random
import re

with open("intents.json") as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()
    user_input = re.sub(r"[^\w\s]", "", user_input)
    user_words = user_input.split()

    best_match = None
    max_score = 0

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_words = pattern.split()
            score = 0

            for word in pattern_words:
                if word in user_words:
                    score += 1

            if score > max_score:
                max_score = score
                best_match = intent

    if best_match and max_score > 0:
        return random.choice(best_match["responses"])

    return "Sorry, I didn't understand that. Could you please rephrase?"