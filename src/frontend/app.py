# You can find this code for Chainlit python streaming here (https://docs.chainlit.io/concepts/streaming/python)

# OpenAI Chat completion
import os
from openai import AsyncClient
import chainlit as cl  # importing chainlit for our app
from chainlit.playground.providers import ChatOpenAI  # importing ChatOpenAI tools
from dotenv import load_dotenv
import asyncio

load_dotenv()

# ChatOpenAI Templates
system_template = """You are a helpful assistant who always speaks in a pleasant tone!
"""

user_template = """{input}
Think through your response step by step.
"""

openai_client = AsyncClient(api_key=os.environ.get("OPENAI_API_KEY"))

@cl.on_chat_start  # marks a function that will be executed at the start of a user session
async def start_chat():
    settings = {
        "model": "gpt-3.5-turbo",
        "temperature": 0,
        "max_tokens": 500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    cl.user_session.set("settings", settings)
    cl.user_session.set(
        "message_history",
        [
            {
                "role": "system",
                "content": system_template,
            }
        ],
    )


async def answer(message: str, settings: dict):
    message_history = cl.user_session.get("message_history")
    msg = cl.Message(content="")

    stream = await openai_client.chat.completions.create(
        messages=message_history + [{"role": "user", "content": user_template.format(input=message)}],
        stream=True,
        **settings,
    )
    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await msg.stream_token(token)

    # Need to add the information that it was the author who answered but OpenAI only allows assistant.
    # simplified for the purpose of the demo.
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()


@cl.on_message  # marks a function that should be run each time the chatbot receives a message from a user
async def main(message: cl.Message):
    settings = cl.user_session.get("settings")
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    await asyncio.gather(answer(message.content, settings))