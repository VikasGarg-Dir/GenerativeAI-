import streamlit as st
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests

# ---------------------- Streamlit UI Setup ---------------------- #
st.set_page_config(page_title="RAG with MongoDB + Ollama", layout="wide")
st.title("🧠 Retrieval-Augmented Generation (RAG) Using MongoDB and Ollama")

# ---------------------- MongoDB and FAISS ---------------------- #
@st.cache_resource
def load_documents():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["rag_collection"]
    collection = db["vikas"]
    return list(collection.find({}))

@st.cache_resource
def build_faiss_index(_docs):
    texts = [doc["rating"] for doc in _docs]
    embeddings = model.encode(texts)
    # print(embeddings)
    dim = embeddings.shape[1]
    # print(dim)
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))
    # print(index)
    return index

def semantic_search(query, index, docs, k=3):
    query_vec = model.encode([query]).astype("float32")
    _, I = index.search(query_vec, k)
    return [docs[i]["rating"] for i in I[0]]

# ---------------------- Ollama Query ---------------------- #
def generate_answer_from_context(query, retrieved_docs):
    context = "\n".join(retrieved_docs)
    
    prompt = f"""
    You are a helpful assistant. You must answer the user's question using only the information provided in the context below.
    If the answer is not found in the context, respond with "I don't know based on the given context."

    --- Context: ---
    {context}

    --- Question: --- 
    {query}

    --- Answer ---
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "deepseek-r1:1.5b",
                "prompt": prompt.strip(),
                "stream": False
            }
        )
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return f"❌ Error: {response.status_code} - {response.text}"
    except requests.exceptions.ConnectionError:
        return "❌ Could not connect to Ollama. Make sure Ollama is running at http://localhost:11434"

# ---------------------- UI Logic ---------------------- #
model = SentenceTransformer("all-MiniLM-L6-v2")
docs = load_documents()
index = build_faiss_index(docs)

query = st.text_input("🔍 Enter your question here:", placeholder="e.g., What is MongoDB indexing?")
# top_k = st.slider("🔎 Number of documents to retrieve:", 1, 10, 3)

if st.button("💬 Get Answer") and query:
    with st.spinner("Retrieving documents and generating answer..."):
        retrieved = semantic_search(query, index, docs)
        answer = generate_answer_from_context(query, retrieved)

        st.markdown("### 📄 Retrieved Context")
        for i, doc in enumerate(retrieved, 1):
            st.markdown(f"**{i}.** {doc}")

        st.markdown("### 🤖 Answer")
        if "I don't know" in answer:
            st.warning(answer)
        else:
            st.success(answer)