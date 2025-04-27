# Importing the necessary libraries
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

# Function to retrieve the relavant context
def retrieve_relevant_context(query, top_k=3):
    chroma_client = PersistentClient(path="./chroma_store")
    collection = chroma_client.get_collection(name="my_collection")
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    query_embedding = model.encode([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results["documents"][0]

