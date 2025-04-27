# Importing the necessary libraries
import os
import chromadb
from chromadb import PersistentClient
import uuid
import pypdf
from sentence_transformers import SentenceTransformer
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import sys
import pysqlite3

# Ensure that sqlite3 is replaced with pysqlite3
sys.modules['sqlite3'] = pysqlite3

# Initialize ChromaDB client
chroma_client = PersistentClient(path="./chroma_store")
collection = chroma_client.get_or_create_collection(name="my_collection")


# Load the text from pdf
def load_pdf(file_path):
    reader = pypdf.PdfReader(file_path)
    pdf_content = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return pdf_content


# Creating the chunks
def chunking(text, chunk_size=3):
    sentences = sent_tokenize(text)
    chunks = []
    for i in range(0, len(sentences), chunk_size):
        chunk = " ".join(sentences[i:i + chunk_size])
        chunks.append(chunk)
    return chunks


# Ingest text and store embeddings
def ingest_document(file_path):
    text = load_pdf(file_path)
    chunks = chunking(text)
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(chunks).tolist()
    ids = [str(uuid.uuid4()) for _ in chunks]
    collection.add(documents=chunks, embeddings=embeddings, ids=ids)
    # print(f"Ingested {len(chunks)} from {file_path}")