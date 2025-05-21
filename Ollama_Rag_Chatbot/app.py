import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

# App Title
st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("🧠 RAG Chatbot with Ollama")
st.markdown("Ask questions based on your ingested PDF documents.")

# Input box for user query
user_input = st.text_input("Enter your question:", "")

if st.button("Get Answer") and user_input.strip() != "":
    with st.spinner("Thinking..."):
        try:
            # Calling FastAPI backend
            response = requests.post(API_URL, json={"query_text": user_input})
            if response.status_code == 200:
                data = response.json()
                st.success(data["response"])
                
                # if data.get("sources"):
                #     st.markdown("#### 🔍 Sources (document IDs):")
                #     st.write(", ".join(str(src) for src in data["sources"] if src))
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to API: {e}")