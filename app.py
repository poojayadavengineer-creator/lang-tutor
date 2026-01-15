import streamlit as st
from llm import get_answer

st.set_page_config(page_title="Python Teacher Bot", page_icon="🐍")

st.title("🐍 Python Teacher Chatbot")
st.caption("Ask me anything about Python. I teach step by step.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Ask a Python question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    try:
        answer = get_answer(user_input)
        print("Answer from get_answer:", answer)  # Debugging line

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)
    except Exception as e:
        st.error(f"Error: {e}")
        print(f"Error during get_answer: {e}")  # Debugging line