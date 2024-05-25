# You can find this code for Chainlit python streaming here (https://docs.chainlit.io/concepts/streaming/python)

# OpenAI Chat completion
# import os
# from openai import AsyncClient
# from chainlit.playground.providers import ChatOpenAI  # importing ChatOpenAI tools
from dotenv import load_dotenv
import streamlit as st
# import asyncio

load_dotenv()

st.header("Welcome to the app!")