import os

import openai

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Sett OPENAI_API_KEY som en miljo-variabel for du starter scriptet.")

openai.api_key = api_key

selected_model = "gpt-3.5-turbo"
# Initialize the list of messages
messages = [{"role": "system", "content": "You are a helpful assistant."}]


# Start a chat
def continue_chat(user_message):
    # Add the user's message to the list
    messages.append({"role": "user", "content": user_message})

    # Get the chat response
    response = openai.chat.completions.create(
        model=selected_model,
        messages=messages,  # the list of all messages
    )
    # Add the AI's response to the list
    messages.append(
        {"role": "assistant", "content": response.choices[0].message.content}
    )

    return response.choices[0].message.content


# Chat with the bot
while True:
    user_message = input("You: ")
    if user_message.lower() == "quit":
        break

    ai_response = continue_chat(user_message)
    print("AI: ", ai_response)
