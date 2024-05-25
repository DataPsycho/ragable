# You can find this code for Chainlit python streaming here (https://docs.chainlit.io/concepts/streaming/python)

# OpenAI Chat completion
# import os
# from openai import AsyncClient
import chainlit as cl  # importing chainlit for our app
from chainlit.message import Message
# from chainlit.playground.providers import ChatOpenAI  # importing ChatOpenAI tools
from dotenv import load_dotenv
# import asyncio

load_dotenv()

@cl.on_message
async def main(message: Message):
   # Your custom logic goes here…
   # Send a response back to the user
   await cl.Message(content=message.content).send()