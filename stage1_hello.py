import os
from google import genai

# Initialize the client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Send a single message to Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello! Who are you?"
)

# Print the response
print(response.text)