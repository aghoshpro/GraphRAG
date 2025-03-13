from langchain_community.embeddings import OllamaEmbeddings
import pandas as pd
import numpy as np
import streamlit as st

def generate_embeddings(text):
    """Generate embeddings for text using Ollama."""
    try:
        embeddings = OllamaEmbeddings(
            model="mxbai-embed-large", 
            base_url="http://localhost:11434",
            show_progress=True
        )
        st.info("Attempting to connect to Ollama service...")
    except Exception as e:
        st.warning("Ollama embeddings service not available. Using fallback random embeddings for demonstration.")
        return _generate_fallback_embeddings(text)

    try:
        if isinstance(text, str):
            return embeddings.embed_query(text)
        elif isinstance(text, pd.DataFrame):
            # For structured data, concatenate all text fields
            text_content = ' '.join(text.astype(str).values.flatten())
            return embeddings.embed_query(text_content)
        else:
            raise ValueError("Unsupported data type for embedding generation")
    except Exception as e:
        st.warning(f"Using fallback embeddings: {str(e)}")
        return _generate_fallback_embeddings(text)

def _generate_fallback_embeddings(text, dim=384):
    """Generate fallback random embeddings when Ollama is not available."""
    st.info("Using demonstration mode with random embeddings.")
    np.random.seed(42)  # For reproducibility
    return np.random.rand(dim).tolist()