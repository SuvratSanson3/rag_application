import streamlit as st
import tempfile
import os
from ingest import ingest_document
from retrieve import retrieve_relevant_context
from generate import generate_answer

st.set_page_config(page_title="Semantic Search & QA (Llama 3 & ChromaDB)", page_icon="📄", layout="centered")
st.title("📄 Semantic Search & QA (Llama 3 & ChromaDB)")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF Document", type= "pdf")

# Text input for user query
query = st.text_input("Enter your Question: ")

# Submit Button
if st.button("Get Answer"):
    if uploaded_file is not None and query:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        try:
            # Ingest the uploaded document
            with st.spinner('Ingesting document...'):
                ingest_document(temp_file_path)
            
            # Retrieve Relevant Context
            with st.spinner('Retrieving relevant context...'):
                docs = retrieve_relevant_context(query)
            
            # Generate an Answer
            with st.spinner('Generating answer...'):
                answer = generate_answer(query, docs)
            
            st.success("Answer:")
            st.write(answer)
        
        finally:
            # Clean up the temporary file
            os.remove(temp_file_path)
    
    else:
        st.warning("Please upload a PDF and enter a question to proceed.")