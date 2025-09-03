import pypdf
from langchain_community.llms.ollama import Ollama
from langchain.chains import RetrievalQA 
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

# Load the dataset 
loader = PyPDFLoader('Linear Regression Based interview Questions (1).pdf')
document = loader.load()

# split into text
text_spliter = CharacterTextSplitter(chunk_size = 500,chunk_overlap = 20)
docs = text_spliter.split_documents(document)

# Embedding
embedding = OllamaEmbeddings(model = 'mxbai-embed-large')

# Vector DB
vectordb = Chroma.from_documents(documents=docs,
                                 embedding=embedding)

# Load ollama Model
llm = Ollama(model = 'deepseek-r1:1.5b')

# Build Retrivel Chian

qa_chain = RetrievalQA.from_chain_type(llm = llm,
                                       chain_type = 'stuff',
                                       retriever = vectordb.as_retriever())

# ask a question
while True:
    query = input("Ask a question: ")
    if query.lower() == 'exit':
        break
    result = qa_chain.invoke(query)
    print(result)