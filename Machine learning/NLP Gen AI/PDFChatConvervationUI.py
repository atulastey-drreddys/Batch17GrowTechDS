import streamlit as st
import google.generativeai as genai
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_commintiy.ve import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# API Configuration
gemini_api = "AIzaSyAYRSbisbijk-vcJ6CIhf1Ytf4RyJJOaX0"
genai.configure(api_key=gemini_api)
model = genai.GenerativeModel('gemini-1.5-flash')

# PDF Loader
loader = PyPDFLoader('my_paper.pdf')
data = loader.load()

# Text Splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,
                                               chunk_overlap = 20)
doc = text_splitter.split_documents(data)

# Vector embedding and vercor storev
vectorstore = Chroma(documents = doc,
                     embedding = GoogleGenerativeAIEmbeddings(model = "model/embedding-001"))

# Retriver
retriever = vectorstore.as_retriever(search_type = 'similarity')

# define

llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash')

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
    print(respones["answer"])

    st.write(respones['answer'])