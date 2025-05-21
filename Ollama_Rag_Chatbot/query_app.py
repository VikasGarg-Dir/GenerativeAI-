import argparse
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function

app = FastAPI()

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context: {context}
---
Answer the question based on the above context: {question}
"""

class QueryRequest(BaseModel):
    query_text: str

@app.post("/")
def read_root():
    return {"Hello": "World"}

@app.post("/query")
async def query_rag(query: QueryRequest):
    query_text = query.query_text

    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="mistral:7b")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]

    formatted_response = f"Response: {response_text}"
    return {"response": formatted_response, "sources": sources}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("query-app:app", host="0.0.0.0", port=8000)

# uvicorn query-app:app --host 127.0.0.1 --port 8000
# ngrok http 8000