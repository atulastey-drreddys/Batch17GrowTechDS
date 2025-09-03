import streamlit as st
from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Initialize the Ollama model (must be running)
llm = Ollama(model="gemma")  # Change to "llama2", "mistral", etc. if needed

# Session memory for chat history
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

# Conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory,
    verbose=False
)

# Streamlit UI
st.title("🧠 Local Chatbot using Ollama + LangChain")

user_input = st.chat_input("Ask me anything...")

if user_input:
    # Generate response
    response = conversation.run(user_input)

    # Display messages
    st.chat_message("user").markdown(user_input)
    st.chat_message("assistant").markdown(response)

