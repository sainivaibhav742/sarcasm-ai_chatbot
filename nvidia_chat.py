import requests
from config import NVIDIA_API_KEY, NVIDIA_API_URL, NVIDIA_MODEL

def chat_with_nvidia(user_input):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {NVIDIA_API_KEY}"
    }

    data = {
        "model": NVIDIA_MODEL,
        "messages": [
            {"role": "system", "content": "You are a sarcastic, witty chatbot who roasts users playfully."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.8,
        "max_tokens": 200,
        "stream": False
    }

    try:
        response = requests.post(NVIDIA_API_URL, headers=headers, json=data)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error talking to NVIDIA: {e}"
