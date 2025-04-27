import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Loading the Groq Key
load_dotenv("key.env")
groq_api_key = os.getenv("chatbot_api_key")

# Initializing the LLM
llm = ChatGroq(groq_api_key=groq_api_key, model="llama-3.3-70b-versatile")

# Function to generate response
def generate_answer(query, context_docs):
    context = "\n".join(context_docs)
    prompt = f"Answer the question based on the following documnets:\n{context}\n\nQuestion: {query}\nAnswer:"
    response = llm.invoke(prompt)
    return response.content.strip()