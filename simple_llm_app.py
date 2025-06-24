import streamlit as st
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="Simple AI Chat", page_icon="💬", layout="wide")
st.title("💬 Simple AI Chat")
st.subheader("A simple AI chat using Streamlit, Ollama and Docker.")

if st.button("Reset Chat", type="primary"):
    st.session_state.pop("chat_histories", None)

if "configurables" not in st.session_state:
    st.session_state.configurables =  {"session_id": "default_session"}

if "sessions" not in st.session_state:
    st.session_state.sessions =  {}

def get_by_session_id(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state.sessions:
         st.session_state.sessions[session_id] = InMemoryChatMessageHistory()
    return st.session_state.sessions[session_id]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a concise and straightfoward assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

if "chain" not in st.session_state:
    llm = ChatOllama(
        model="llama3.2",
        base_url="http://localhost:11434",
        temperature=0.3,
        max_tokens=50
    )
    chain = prompt | llm

    st.session_state.chain = RunnableWithMessageHistory(
        chain,
        get_by_session_id,
        input_messages_key="question",
        history_messages_key="history",
    )
    
history = get_by_session_id("default_session")

for idx, msg in enumerate(history.messages):
    if idx > 0 and idx % 2 == 0:
        st.divider()
    if isinstance(msg, HumanMessage):
        st.markdown(f"**You :** {msg.content}")
    elif isinstance(msg, AIMessage):
        st.markdown(f"**AI :** {msg.content}")

if prompt_input := st.chat_input("Tip your message..."):
    response = st.session_state.chain.invoke(
        {"question": prompt_input},
        config=st.session_state.configurables
    )
    response_text = response.content if hasattr(response, "content") else str(response)

    st.divider()
    st.markdown(f"**You :** {prompt_input}")
    st.markdown(f"**AI :** {response_text}")