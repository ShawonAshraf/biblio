"""
sets up an llm based client and defines related operaitons
filename inspired from the Armored Core VI character, Handler Walter
"""

import instructor
import openai
import os
from database.schemas import BookBase
from loguru import logger


# using ollama as the default provider
# the provider has to be openai compatible
LLM_PROVIDER_URL = os.getenv("LLM_PROVIDER_URL", "http://gandalf:11434/v1")
# mistral is the default model, used from ollama
MODEL_NAME = os.getenv("MODEL_NAME", "calebfahlgren/natural-functions")
# in case of using openai models
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "ollama")


# setup an instructor client for json mode
def setup():
    logger.info("setting up instructor client")
    logger.info(f"using provider: {LLM_PROVIDER_URL}")

    client = instructor.from_openai(
        openai.OpenAI(
            base_url=LLM_PROVIDER_URL,
            api_key=OPENAI_API_KEY,
        ),
        mode=instructor.Mode.JSON,
    )

    return client


def add_book(client, instruction: str) -> dict:
    # prompt
    messages = [
        {
            "role": "system",
            "content": "You're an AI assistant who returns book details in json format.",
        },
        {"role": "user", "content": instruction},
    ]

    logger.info(f"sending instruction: {instruction}")
    logger.info(f"using model: {MODEL_NAME}")

    response = client.chat.completions.create(
        model=MODEL_NAME, messages=messages, temperature=0.0, response_model=BookBase
    )

    # return as json
    return response.model_dump_json(indent=4)
