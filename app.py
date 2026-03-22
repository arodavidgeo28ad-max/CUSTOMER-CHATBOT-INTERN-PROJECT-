from flask import Flask, request, jsonify, render_template_string
import chatbot
import os

app = Flask(__name__)

# Load the HTML template once at startup
HTML_FILE = 'index.html'

def get_html_content():
    if os.path.exists(HTML_FILE):
        with open(HTML_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    return "<h1>Error: index.html not found</h1>"

@app.route('/')
def home():
    return render_template_string(get_html_content())

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"response": "I didn't receive a message."}), 400
    
    response = chatbot.get_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
