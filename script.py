import os
from dotenv import load_dotenv
from mistralai import Mistral


load_dotenv()
api_key= os.environ["API_KEY"]
model= "mistral-small-latest"

client= Mistral(api_key=api_key)


def get_response(content):
    chat_response= client.chat.complete(
        model= model,
        messages= [
            {
                "role": "system",
                "content": "My chatbot assistent for code. Remember that I'm using EndevourOS"
            },
            {
                "role": "user",
                "content": content
            }
        ]
    )
    return chat_response.choices[0].message.content



