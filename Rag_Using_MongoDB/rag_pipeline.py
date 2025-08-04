from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests

# ------------------ MongoDB Connection ------------------ #
client = MongoClient("mongodb://localhost:27017/")
db = client["sample_rag_data"]
collection = db["sample_db"]

# ------------------ Embedding Model ------------------ #
model = SentenceTransformer("all-MiniLM-L6-v2")

# ------------------ Build FAISS Index ------------------ #
def build_faiss_index():
    docs = list(collection.find({}))
    texts = [doc["content"] for doc in docs]
    embeddings = model.encode(texts)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype('float32'))

    return index, docs

# ------------------ Semantic Search ------------------ #
def semantic_search(query, index, docs, k=3):
    query_vec = model.encode([query]).astype('float32')
    _, I = index.search(query_vec, k)

    results = [docs[i]["content"] for i in I[0]]
    return results

# ------------------ Generate Answer via Ollama ------------------ #
def generate_answer(query, retrieved_docs):
    context = "\n".join(retrieved_docs)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "deepseek-r1:1.5b",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# ------------------ Main Entry ------------------ #
if __name__ == "__main__":
    index, docs = build_faiss_index()

    query = input("Enter your question: ")
    relevant_docs = semantic_search(query, index, docs)
    answer = generate_answer(query, relevant_docs)

    print("\n--- Answer ---")
    print(answer)