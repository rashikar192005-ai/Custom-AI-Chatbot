import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Conversation memory
conversation = []

print("Custom AI Chatbot")
print("Type 'exit' to stop.")

while True:
    user_input = input("You: ")

    # Ignore empty input
    if not user_input.strip():
        continue

    # Exit chatbot
    if user_input.lower() == "exit":
        print("Chatbot stopped.")
        break

    # Store user message
    conversation.append({
        "role": "user",
        "content": user_input
    })

    # Send conversation to AI
    try:
        response = client.responses.create(
            model="gpt-5.6",
            input=conversation
        )

        ai_response = response.output_text

    except Exception as e:
        print("API Error:", e)
        ai_response = "Sorry, the AI service is currently unavailable."

    # Store AI response
    conversation.append({
        "role": "assistant",
        "content": ai_response
    })

    print("AI:", ai_response)