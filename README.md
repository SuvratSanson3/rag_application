# RAG Application

A simple **RAG (Retrieval-Augmented Generation)** application that lets users upload a PDF, ask questions, and get AI-generated answers.

- **Model:** Llama 3.3-70B Versatile
- **Vector Store:** ChromaDB for semantic search
- **Frontend:** Streamlit
- **Backend:** Python

## Features
- Upload your own PDF documents
- Ask questions related to the PDF
- Get intelligent, context-based answers powered by LLM + retrieval

## Tech Stack
- [Llama 3.3-70B Versatile](https://groq.com/)
- [ChromaDB](https://docs.trychroma.com/)
- [Streamlit](https://streamlit.io/)
- Python 3.12

## Installation
```bash
# Clone the repo
git clone https://github.com/your-username/rag_application.git
cd rag_application

# Create and activate virtual environment
python -m venv rag_env
source rag_env/bin/activate    # (Linux/macOS)
rag_env\Scripts\activate       # (Windows)

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py
