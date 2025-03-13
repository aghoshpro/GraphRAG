import networkx as nx
from neo4j import GraphDatabase
import streamlit as st
import pandas as pd
import os

class GraphManager:
    def __init__(self):
        self.uri = os.environ["NEO4J_URI"]
        self.auth = (os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"])  # Should be moved to environment variables
        self.driver = None

        

    def get_neo4j_connection(self):
        """Establish Neo4j connection with error handling."""
        if not self.driver:
            try:
                self.driver = GraphDatabase.driver(self.uri, auth=self.auth)
                # Test the connection
                with self.driver.session() as session:
                    session.run("RETURN 1")
            except Exception as e:
                st.warning("Neo4j connection failed. Operating in local mode only.")
                return None
        return self.driver

    def update_graph(self, data):
        """Update knowledge graph with new data."""
        graph = nx.Graph()

        try:
            if isinstance(data, pd.DataFrame):
                # Process structured data
                self._process_structured_data(data, graph)
            else:
                # Process unstructured data
                self._process_unstructured_data(data, graph)

            # Try to store in Neo4j if available
            if self.get_neo4j_connection():
                self._store_in_neo4j(graph)

            return graph
        except Exception as e:
            st.error(f"Error updating graph: {str(e)}")
            return nx.Graph()  # Return empty graph on error

    def _process_structured_data(self, df, graph):
        """Process structured data and add to graph."""
        for _, row in df.iterrows():
            for col in df.columns:
                graph.add_node(str(row[col]))
                if col != df.columns[0]:
                    graph.add_edge(str(row[df.columns[0]]), str(row[col]))

    def _process_unstructured_data(self, text, graph):
        """Process unstructured text and add to graph."""
        # Basic implementation - should be enhanced with proper NER
        words = text.split()
        for i in range(len(words)-1):
            graph.add_edge(words[i], words[i+1])

    def _store_in_neo4j(self, graph):
        """Store graph in Neo4j database."""
        driver = self.get_neo4j_connection()
        if not driver:
            return

        with driver.session() as session:
            try:
                # Clear existing graph
                session.run("MATCH (n) DETACH DELETE n")

                # Add nodes
                for node in graph.nodes():
                    session.run(
                        "CREATE (n:Entity {name: $name})",
                        name=str(node)
                    )

                # Add relationships
                for edge in graph.edges():
                    session.run(
                        """
                        MATCH (a:Entity {name: $name1})
                        MATCH (b:Entity {name: $name2})
                        CREATE (a)-[:RELATED_TO]->(b)
                        """,
                        name1=str(edge[0]),
                        name2=str(edge[1])
                    )
            except Exception as e:
                st.error(f"Error storing in Neo4j: {str(e)}")