from langchain_community.llms import Ollama
from langchain.chains import GraphQAChain
import streamlit as st

class QueryProcessor:
    def __init__(self):
        try:
            self.llm = Ollama(model="llama3.2", base_url="http://localhost:11434")
        except Exception as e:
            st.warning("Ollama LLM not available. Please ensure Ollama is running locally.")
            self.llm = None

    def process_query(self, query, graph):
        """Process natural language query using Langchain and graph data."""
        if not self.llm:
            return "LLM is not available. Please ensure Ollama is running locally and refresh the page."

        try:
            # Create a GraphQAChain
            chain = GraphQAChain.from_llm(
                llm=self.llm,
                graph=graph,
                verbose=True
            )

            # Execute query
            response = chain.run(query)

            return response

        except Exception as e:
            st.error(f"Query processing failed: {str(e)}")
            return f"Error processing query: {str(e)}"