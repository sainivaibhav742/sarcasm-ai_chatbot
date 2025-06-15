from flask import Flask, request, jsonify, render_template
from groq_chat import chat_with_groq

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Loads the HTML page

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    bot_reply = chat_with_groq(user_message)
    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
