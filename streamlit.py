import os
import streamlit as st
from openai import OpenAI, chat
from dotenv import load_dotenv

# Load environment variables
load_dotenv("test.env")

# Get the OpenAI API key
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Check if the API key is set
if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment file")

# Initialize the OpenAI client with the API key
openai = OpenAI(api_key=openai_api_key)

st.title("Hello! User ")
st.subheader("How can I help You 😊?")

if "openai_model" not in st.session_state:
  st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    message_placeholder = st.empty()

    # Create a chat completion request
    completion = chat.completions.create(
        model=st.session_state["openai_model"],
        messages=[
            {"role": "system", "content": "You are a Mathematical,news,therapy,tourism,map,psychological,supportive,coding,science,technological,service-oriented,no-illegal assistant, skilled in explaining complex programming concepts in  a creative manner"},
            {"role": "user", "content": prompt}
        ]
    )

    full_response = completion.choices[0].message.content
    message_placeholder.markdown(full_response)

  st.session_state.messages.append({"role": "assistant", "content": full_response})