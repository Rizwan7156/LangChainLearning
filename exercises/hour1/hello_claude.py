from dotenv import load_dotenv
import os

from anthropic import Anthropic

# STEP 1
load_dotenv()

# STEP 2
api_key = os.getenv("ANTHROPIC_API_KEY")

print("=== HOUR 1 - HELLO MODEL ===")

if not api_key:
    raise ValueError(
        "Claude API Key not found"
    )

# STEP 3
client = Anthropic(
    api_key=api_key
)

print("Claude Client Created")

# STEP 4 - List models available to this API key
print("\nAvailable models for this API key:")
for model in client.models.list().data:
    print(f"  - {model.id}")

# STEP 5 - Send a message using a current model
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content":
            "Introduce yourself in exactly 3 lines."
        }
    ]
)

# STEP 6
print("\nClaude Response:\n")

print(
    message.content[0].text
)