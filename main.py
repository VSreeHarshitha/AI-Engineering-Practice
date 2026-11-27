"""from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

history = []

while True:
    user_input = input("Ask your question: ")

    if user_input.lower() == "exit":
        break

    history.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    print(history)

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=history
    )

    print(response.text)

    history.append({
        "role": "model",
        "parts": [{"text": response.text}]
    })
    print(response.response_id)"""
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

chat = client.chats.create(model="gemini-3.5S-flash")

while True:
    user_input = input("Ask your question: ")

    if user_input.lower() == "exit":
        break

    response = chat.send_message(user_input)

    print(response.text)