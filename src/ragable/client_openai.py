import os
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai import OpenAI
from dotenv import load_dotenv
from ragable.utils.reach_print import display_message


def system_prompt(message: str) -> dict:
    return {"role": "system", "content": message}


def assistant_prompt(message: str) -> dict:
    return {"role": "assistant", "content": message}


def user_prompt(message: str) -> dict:
    return {"role": "user", "content": message}


def get_response(client: OpenAI, messages: str, model: str = "gpt-3.5-turbo") -> str:
    return client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )


def extract_message(response: ChatCompletion) -> None:
    message: ChatCompletionMessage = response.choices[0].message
    return message.content


if __name__ == "__main__":
    load_dotenv(override=True)
    PROMPT = "What is the difference between LangChain and LlamaIndex?"
    messages = [
        system_prompt("You are joyful and having an awesome day!"),
        user_prompt("What is the difference between LangChain and LlamaIndex?"),
    ]
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = get_response(client, messages)
    message = extract_message(response)
    display_message(message)
