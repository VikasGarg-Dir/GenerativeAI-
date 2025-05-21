import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


from langchain_community.embeddings.ollama import OllamaEmbeddings


def get_embedding_function():
    embeddings = OllamaEmbeddings(model="mistral:7b")
    return embeddings
