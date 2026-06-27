from dotenv import load_dotenv
from anthropic import Anthropic
import os

load_dotenv()

client = Anthropic()

api_key = os.getenv("ANTHROPIC_API_KEY")

print(api_key is not None)

messages = []

def ask_claude(prompt):

    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=messages
    )

    assistant_text = response.content[0].text

    messages.append(
        {
            "role": "assistant",
            "content": assistant_text
        }
    )

    print("\n--- TOKEN USAGE ---")
    print(f"Input Tokens:  {response.usage.input_tokens}")
    print(f"Output Tokens: {response.usage.output_tokens}")
    print("-------------------\n")

    return assistant_text


while True:

    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        break

    response = ask_claude(user_input)

    print("\nClaude:")
    print(response)




