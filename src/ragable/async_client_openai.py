from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv(override=True)

client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant who always speaks in a pleasant tone!"},
        {"role": "user", "content": "What is the difference between LangChain and LlamaIndex?"},
    ],
    temperature=0,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

result = asyncio.get_event_loop().run_until_complete(response)
print(result)