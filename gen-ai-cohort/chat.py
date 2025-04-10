import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # this loads variables from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
       {role:"system","content": "you are an assistant"},
        {role:"user","content": "what is LRU cache?"}
    ],
)

print(completion.choices[0].message.content)