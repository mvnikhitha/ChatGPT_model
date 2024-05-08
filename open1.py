
import dotenv
from openai import OpenAI
import os
#client = openai()
#os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
from openai import OpenAI, chat
from dotenv import load_dotenv

load_dotenv("openai.env")
client = OpenAI(
    api_key=os.environ.get("C:\\Users\\mvnik\\openai\\openai.env"),
 )
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  
  messages=[
    {"role": "system", "content": "You are a mathematical assistant, skilled in explaining complex programming concepts"},
    {"role": "user", "content": input("what is your question?")}
  ]
)
print(completion.choices[0].message.content)