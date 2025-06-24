import streamlit as st

st.set_page_config(page_title="Simple LLM", page_icon="💬", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 Simple LLM Chat")
st.subheader("An simple LLM Chat using Langchain and Ollama")

if st.button("Reset Chat", type="primary"):
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Tip your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = f"You: **{prompt}** LLM RESPONSE HERE"

    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
