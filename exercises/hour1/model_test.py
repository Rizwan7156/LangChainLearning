from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

print("Claude Client Created Successfully")