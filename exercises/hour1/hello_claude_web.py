from dotenv import load_dotenv
import os

import streamlit as st
from anthropic import Anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

st.set_page_config(
    page_title="Hour 1 Claude Demo"
)

st.title("🤖 Hour 1 Claude Demo")

if not api_key:
    st.error("API Key Not Found")
    st.stop()

client = Anthropic(
    api_key=api_key
)

st.success("Claude API Connected")

if st.button("Call Claude"):

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": "Introduce yourself in 3 lines."
            }
        ]
    )

    st.write(
        message.content[0].text
    )