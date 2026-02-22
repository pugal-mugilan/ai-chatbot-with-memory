import os
import json
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

MEMORY_FILE = "chat_history.json"

SYSTEM_PROMPT = """You are a helpful and concise assistant for a software developer 
who is learning AI engineering. When explaining concepts, always relate 
them back to software engineering principles he already knows. Be encouraging but direct.
Keep responses focused and practical."""


def load_history():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
            # Convert raw dicts back into types.Content objects
            return [
                types.Content(
                    role=msg["role"],
                    parts=[types.Part(text=p["text"]) for p in msg["parts"]]
                )
                for msg in data
            ]
    return []


def save_history(history):
    # Convert types.Content objects into plain dicts for JSON storage
    data = [
        {
            "role": msg.role,
            "parts": [{"text": p.text} for p in msg.parts]
        }
        for msg in history
    ]
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def chat(history, user_input):
    history.append(
        types.Content(role="user", parts=[types.Part(text=user_input)])
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )

    reply = response.text

    history.append(
        types.Content(role="model", parts=[types.Part(text=reply)])
    )

    return reply, history


def main():
    history = load_history()

    if history:
        print(f"📂 Loaded {len(history)} messages from previous session.\n")
    else:
        print("🆕 Fresh conversation started.\n")

    print("🤖 Gemini Chatbot — type 'quit' to exit, 'clear' to reset memory\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["quit", "exit", "q"]:
            save_history(history)
            print("💾 Conversation saved. Goodbye!")
            break

        if user_input.lower() == "clear":
            history = []
            if os.path.exists(MEMORY_FILE):
                os.remove(MEMORY_FILE)
            print("🗑️  Memory cleared.\n")
            continue

        if not user_input:
            continue

        reply, history = chat(history, user_input)
        print(f"\nGemini: {reply}\n")
        save_history(history)


if __name__ == "__main__":
    main()