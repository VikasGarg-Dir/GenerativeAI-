# 🤖 RAG Chatbot using Ollama, FastAPI, ChromaDB & Streamlit

A powerful, privacy-focused **Retrieval-Augmented Generation (RAG)** chatbot pipeline that runs **entirely on your local machine** using **Ollama**, served via **FastAPI**, retrieved via **ChromaDB**, and visualized with a slick **Streamlit UI**. Perfect for querying PDF documents with real-time answers from local LLMs like Mistral, LLaMA2 or Deepseek.

---

## 🚀 Key Features

* ✅ **Local LLMs via Ollama** – No external API keys, full control
* ✅ **FastAPI Backend** – Lightweight, high-performance REST API
* ✅ **Chroma Vector DB** – Efficient semantic document search
* ✅ **PDF Ingestion** – Drag-and-drop PDF processing
* ✅ **Streamlit UI** – Interactive front-end for real-time Q\&A
* ✅ **Fully Modular & Scalable** – Clean architecture for production-readiness

---

## 🧠 Tech Stack

| Layer         | Technology               |
| ------------- | ------------------------ |
| Backend API   | FastAPI                  |
| Frontend      | Streamlit                |
| Vector Store  | ChromaDB                 |
| LLM Inference | Ollama (Mistral, LLaMA2) |
| Language      | Python 3.11              |
| Deployment    | Localhost / Ngrok        |

---

## 📁 Folder Structure

```
Rag_Chatbot_using_Ollama/
├── chroma/                   # Vector database files
├── data/                     # Input PDF documents
├── get_embedding_function.py # Embedding function logic
├── populate_database.py      # PDF ingestion to Chroma
├── query-app.py              # FastAPI backend
├── app.py                    # Streamlit UI
├── document_log.json         # Logs of processed PDFs
├── requirements.txt          # Python dependencies
└── .gitignore
```

---

## 🛠️ Setup & Installation

1. **Clone the repo**

```bash
git clone https://github.com/anish3565/Rag_Chatbot_using_Ollama.git
cd Rag_Chatbot_using_Ollama
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install and start Ollama**

👉 Follow: [https://ollama.ai](https://ollama.ai)
📦 Recommended model: `mistral`

```bash
ollama run mistral
```

---

## ⚙️ How to Run

### 1. Add your PDFs

Place your documents in the `data/` folder.

### 2. Ingest PDFs into Chroma

```bash
python populate_database.py
```

### 3. Start the FastAPI server

```bash
uvicorn query-app:app --reload
```

API will be live at `http://127.0.0.1:8000`

### 4. Launch the Streamlit chatbot UI

```bash
streamlit run app.py
```

🎉 Now ask questions in your browser at `http://localhost:8501`

---

---

## 🌍 Optional: Public Exposure via ngrok

```bash
ngrok http 8000
```

Use the generated URL in your frontend or to share the chatbot API externally.

---

## 🔧 Skills Demonstrated

 **🧠 Machine Learning**: RAG pipeline implementation
* **🧾 NLP & Embeddings**: Document embedding + semantic retrieval
* **🔗 Backend Engineering**: FastAPI for serving model and retrieval
* **🖼️ Frontend Prototyping**: Streamlit UI for user interaction
* **📄 Document Processing**: PDF ingestion pipeline
* **📦 Software Architecture**: Modular, readable, scalable structure

---

## 🔮 Future Enhancements

* 🔐 Add user authentication and session memory
* ☁️ Migrate to AWS/GCP for scalable cloud deployment
* 🎯 Add filters for document-specific queries
* 📊 Streamlit+Plotly visual summaries for document insights

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

> 🌟 **Star this repo** if you find it helpful.
> ✉️ [Let’s connect on LinkedIn](https://www.linkedin.com/in/anishnsut) for collaborations!
