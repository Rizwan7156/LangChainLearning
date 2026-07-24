from dotenv import load_dotenv
import os

import streamlit as st
from anthropic import Anthropic

# -----------------------------
# Load Environment
# -----------------------------

load_dotenv()

api_key = os.getenv(
    "ANTHROPIC_API_KEY"
)

if not api_key:

    st.error(
        "Claude API Key Not Found"
    )

    st.stop()

# -----------------------------
# Claude Client
# -----------------------------

client = Anthropic(
    api_key=api_key
)

# -----------------------------
# Browser UI
# -----------------------------

st.set_page_config(
    page_title="Hours 4-5 Claude Chatbot"
)

st.title(
    "💬 Hours 4-5 Claude Streaming Chatbot"
)

st.success(
    "Claude API Connected"
)

# -----------------------------
# System Role
# -----------------------------

system_prompt = st.text_area(
    "System Message",
    "You are a helpful AI assistant."
)

# -----------------------------
# Message History
# -----------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []

# Display Chat History

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):

        st.write(
            msg["content"]
        )

# -----------------------------
# User Message
# -----------------------------

user_prompt = st.chat_input(
    "Ask something..."
)

if user_prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message(
        "user"
    ):
        st.write(user_prompt)

    # Claude Call

    conversation = []

    for msg in st.session_state.messages:

        if msg["role"] == "user":

            conversation.append(
                {
                    "role": "user",
                    "content": msg["content"]
                }
            )

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        system=system_prompt,
        max_tokens=500,
        messages=conversation
    )

    assistant_reply = (
        response.content[0].text
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    with st.chat_message(
        "assistant"
    ):
        st.write(
            assistant_reply
        )