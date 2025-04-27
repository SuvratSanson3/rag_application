from ingest import ingest_document
from retrieve import retrieve_relevant_context
from generate import generate_answer

file_path = "/home/abcom/Downloads/sample_ai_intro.pdf"

query = "What are the key points that can be derived from the document?"

ingest_document(file_path)

docs = retrieve_relevant_context(query)

answer = generate_answer(query, docs)

print(f"Answer: {answer}")


