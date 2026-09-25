# Custom AI Chatbot with Memory

## Project Overview

This project is a conversational AI chatbot that maintains conversation history during a live session.

The chatbot stores user messages and AI responses in an in-memory list so that previous conversation context can be maintained.

## Technologies Used

- Python
- OpenAI API
- OpenAI Python SDK
- python-dotenv

## Key Features

- Interactive terminal-based chatbot
- Conversation memory using a Python list
- Stores user messages and AI responses
- API integration with an AI model
- Handles API errors without crashing
- Exit option to stop the chatbot
- Ignores empty user input

## How It Works

1. The user enters a message.
2. The message is added to the conversation history.
3. The conversation history is sent to the AI model.
4. The AI response is received.
5. The AI response is added to the conversation history.
6. The process continues until the user types `exit`.

## Project Structure

```text
Custom-AI-Chatbot/
│
├── chatbot.py
├── README.md
└── .env