"""
interacts with the handler to send instructions to an llm
"""

# https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models

from handler.walter import setup
from loguru import logger
import openai


def add_book(book_name: str, author: str):
    logger.info(f"Adding: {book_name} :: {author}")
    return {"book_name": book_name, "author": author}


if __name__ == "__main__":
    client = openai.Client(base_url="http://localhost:11434/v1", api_key="ollama")

    # r = add_book(client, "add '1984' by 'George Orwell'")

    # print(r)

    tools = [
        # function add_book
        {
            "type": "function",
            "function": {
                "name": "add_book",
                "description": "add a book to the database",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "book_name": {
                            "type": "string",
                            "description": "name of the book",
                        },
                        "author": {
                            "type": "string",
                            "description": "name of the author",
                        },
                    }
                },
                "required": ["book_name", "author"],
            },
        },
        # another one
    ]

    messages = []
    messages.append(
        {
            "role": "system",
            "content": "You're an AI assistant who helps manage a book database.",
        }
    )
    messages.append({"role": "user", "content": "add '1984' by 'George Orwell'"})
# https://ollama.com/calebfahlgren/natural-functions
# https://github.com/cfahlgren1/natural-functions/blob/main/natural-functions-demo.ipynb
    r = client.chat.completions.create(
        model="calebfahlgren/natural-functions",
        messages=messages,
        tools=tools,  # type: ignore
        tool_choice={
            "type": "function",
            "function": {"name": "add_book"},
        },
        temperature=0.0,
    )

    print(r.choices[0].message)
