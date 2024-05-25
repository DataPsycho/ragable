from dotenv import load_dotenv
import streamlit as st
from ragable.client_openai import (
    system_prompt,
    user_prompt,
    get_response,
    extract_message,
)
import os
from openai import OpenAI
import logging
import time
from typing import Generator

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("APP")


load_dotenv()

st.title("Rabable: Your Dream Bot")
SYSTEM_PROMPT = """You are joyful assistance, who can answer numerious questions. 
If you do not know about it simply say that you have no information about it."""


def create_response_from_user_message(message: str) -> Generator:
    messages = [system_prompt(message=SYSTEM_PROMPT), user_prompt(message=message)]
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = get_response(client, messages)
    message = extract_message(response)
    logger.info("Message is created!")
    for word in message.split():
        yield word + " "
        time.sleep(0.05)



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    logger.info(f"User Query: {prompt}")

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        answer = create_response_from_user_message(prompt)
        response = st.write_stream(answer)
        logger.info(f"Assistant reply: {answer}")
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
