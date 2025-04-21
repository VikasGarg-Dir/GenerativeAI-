from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
import os
import shutil
import chromadb
from dotenv import load_dotenv


CHROMA_PATH = "chroma"
DATA_PATH = "files"

load_dotenv()

def create_vector_database():
    
    documents = []
    for file in os.listdir(DATA_PATH):
        if file.endswith('.pdf'):
            PDF_PATH = os.path.join(DATA_PATH, file)
            loader = PyPDFLoader(PDF_PATH)
            documents.extend(loader.load())
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap=100,
        length_function = len,
        add_start_index= True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    
    db = Chroma.from_documents(
        documents=chunks,
        embedding=OpenAIEmbeddings(), 
        persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}")
    
create_vector_database()