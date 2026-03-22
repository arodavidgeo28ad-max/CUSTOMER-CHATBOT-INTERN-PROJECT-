from flask import Flask, request, jsonify, render_template_string
from chatbot import get_response
import os

app = Flask(__name__)

# Load the premium HTML content
try:
    with open("nexus-elite.html", "r", encoding="utf-8") as f:
        NEXUS_HTML = f.read()
except FileNotFoundError:
    NEXUS_HTML = "<h1>Frontend file nexus-elite.html not found!</h1>"

@app.route("/")
def home():
    return render_template_string(NEXUS_HTML)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"response": "I didn't hear anything. Could you please repeat?"})
    
    bot_reply = get_response(user_input)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)