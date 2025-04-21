from fastapi import FastAPI, HTTPException
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import uvicorn

load_dotenv()
CHROMA_PATH = "chroma"

embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

llm = ChatOpenAI(model="gpt-4",temperature=0)

prompt = ChatPromptTemplate.from_template(
    """ Answer the following questions based only on the provided context.
    Think step by step before providing a detailed answer.
    <context>
    {context}
    </context>
    Question: {input}
    """
)

document_chain=create_stuff_documents_chain(llm,prompt)
retriever = db.as_retriever()

retriever_chain = create_retrieval_chain(retriever, document_chain)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/query/")
def query_handler(query: str):
    try:
        result = retriever_chain.invoke({"input": query})
        return {"answer": result['answer']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, port=8000)


