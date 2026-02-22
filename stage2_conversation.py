import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# This list holds the entire conversation history
conversation_history = []

print("🤖 Gemini Chatbot — type 'quit' to exit\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break

    if not user_input:
        continue

    # Add user message to history
    conversation_history.append(
        types.Content(role="user", parts=[types.Part(text=user_input)])
    )

    # Send the FULL history every time — this is how memory works
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation_history
    )

    assistant_reply = response.text

    # Add Gemini's reply to history too
    conversation_history.append(
        types.Content(role="model", parts=[types.Part(text=assistant_reply)])
    )

    print(f"\nGemini: {assistant_reply}\n")