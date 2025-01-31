# README

## OpenAI Chat Assistant with Streamlit

This project demonstrates an AI-powered chat assistant using OpenAI's GPT-3.5 Turbo model, integrated with Streamlit for an interactive user interface.

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Required dependencies:
  ```bash
  pip install openai streamlit python-dotenv
  ```

### Project Setup

1. **Set up Environment Variables**
   - Create a `.env` file (e.g., `test.env`) and add your OpenAI API key:
   ```ini
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   - Alternatively, store it in a local file (`openai.env`) and reference it in the script.

2. **Load Environment Variables**
   ```python
   import os
   from dotenv import load_dotenv
   load_dotenv("test.env")
   ```

3. **Initialize OpenAI Client**
   ```python
   from openai import OpenAI
   openai_api_key = os.environ.get("OPENAI_API_KEY")
   if openai_api_key is None:
       raise ValueError("OPENAI_API_KEY is not set in the environment file")
   openai = OpenAI(api_key=openai_api_key)
   ```

4. **Build the Streamlit Interface**
   ```python
   import streamlit as st
   st.title("Hello! User")
   st.subheader("How can I help you? 😊")
   ```

5. **Handle Chat Messages**
   ```python
   if "messages" not in st.session_state:
       st.session_state.messages = []
   for message in st.session_state.messages:
       with st.chat_message(message["role"]):
           st.markdown(message["content"])
   ```

6. **Process User Input and Generate Responses**
   ```python
   from openai import chat
   if prompt := st.chat_input("What is up?"):
       st.session_state.messages.append({"role": "user", "content": prompt})
       with st.chat_message("user"):
           st.markdown(prompt)
       with st.chat_message("assistant"):
           message_placeholder = st.empty()
           completion = chat.completions.create(
               model="gpt-3.5-turbo",
               messages=[
                   {"role": "system", "content": "You are a multi-functional assistant skilled in various domains like mathematics, programming, news, and psychological support."},
                   {"role": "user", "content": prompt}
               ]
           )
           full_response = completion.choices[0].message.content
           message_placeholder.markdown(full_response)
       st.session_state.messages.append({"role": "assistant", "content": full_response})
   ```

### Running the Application
To start the Streamlit app, use the following command:
```bash
streamlit run your_script.py
```

### Features
- OpenAI API integration for AI-generated responses
- Streamlit-based user-friendly chat UI
- Environment variable management using dotenv
- Multi-functional AI capabilities: programming, psychological support, tourism, and more
