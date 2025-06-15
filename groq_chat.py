import requests
from config import GROQ_API_KEY, GROQ_API_URL, GROQ_MODEL

def chat_with_groq(user_input):
    headers = {
        "Content-Type": "application/json",
    }
    if GROQ_API_KEY:
        headers["Authorization"] = f"Bearer {GROQ_API_KEY}"

    data = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a sarcastic, witty chatbot who roasts users playfully."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.8,
        "max_tokens": 200
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error talking to Groq: {e}"
