import requests

response = requests.post(
    "http://127.0.0.1:5000/chat",
    json={"message": "Roast me"}
)

print("Bot:", response.json()['response'])
