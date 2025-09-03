import streamlit as st
import google.generativeai as genai
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# API Configuration
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# PDF Loader
loader = PyPDFLoader('my_paper.pdf')
data = loader.load()

# Text Splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,
                                               chunk_overlap = 20)
doc = text_splitter.split_documents(data)

# Vector embedding and vercor storev
vectorstore = Chroma.from_documents(documents = doc,
                     embedding = GoogleGenerativeAIEmbeddings(model = "models/embedding-001"))

# Retriver
retriever = vectorstore.as_retriever(search_type = 'similarity')

# define

llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
st.title("Chat With PDF")

query = st.chat_input("Ask me anything: ")
promt = query

system_output = (
    "You ara my personal assistant to talk with PDF"
    "{context}"
)
# Make ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [('system',system_output),
    ("human","{input}")]
)

# Create chains

if query:
    question_answer_chain = create_stuff_documents_chain(llm,prompt)
    rag_chain = create_retrieval_chain(retriever,question_answer_chain)

    respones = rag_chain.invoke({'input':query})
    st.write("User query :",query)
    print(respones["answer"])


    st.write("Chatbot response :",respones['answer'])