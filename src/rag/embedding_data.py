import chromadb
from langchain_ollama import OllamaEmbeddings
from chromadb.utils.embedding_functions import EmbeddingFunction

CHROMA_PATH = r"data/chroma_db"
embeddings = OllamaEmbeddings(
    model="qwen3-embedding"
)
def setup_chroma_db():
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection_name ="Medical_Articles"
    collection = chroma_client.get_or_create_collection(name=collection_name, embedding_function=EmbeddingFunction(
        embed_method=embeddings.embed_query,
        normalize=False
    ))
    return collection

def embed_text(text: str):
    input_text = []
    for content in text:
        input_text.append(content.page_content)
    response = embeddings.embed_documents([input_text[0],input_text[1]])
    print(f"Embedding response: {response}")  # Print the full response for debugging
    return response

def query_chuncks(query: str, collection):
    query_embedding = embeddings.embed_query(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    return results
