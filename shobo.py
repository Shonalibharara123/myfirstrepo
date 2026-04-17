import streamlit as st
import ollama

st.title("💬 Shobo Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display past messages
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# Chat input box (must be only once, with a unique key)
user_input = st.chat_input("Type your message...", key="chatbox")

if user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Query Ollama (Llama3 model)
    response = ollama.chat(model="llama3", messages=st.session_state["messages"])
    bot_reply = response['message']['content']

    # Add assistant reply
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").write(bot_reply)
