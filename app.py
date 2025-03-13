import streamlit as st
import networkx as nx
import pandas as pd
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt # Added import statement
from utils.file_processor import process_file
from utils.graph_manager import GraphManager
from utils.query_processor import QueryProcessor
from utils.embeddings import generate_embeddings

# Initialize session state
if 'graph' not in st.session_state:
    st.session_state.graph = nx.Graph()
if 'data_df' not in st.session_state:
    st.session_state.data_df = pd.DataFrame()
if 'text_content' not in st.session_state:
    st.session_state.text_content = ""

# Page configuration
st.set_page_config(layout="wide", page_title="Knowledge Graph RAG")

# Initialize components
graph_manager = GraphManager()
query_processor = QueryProcessor()

# Sidebar
with st.sidebar:
    st.title("Data Upload")
    uploaded_file = st.file_uploader(
        "Upload your data file",
        type=['txt', 'json', 'csv', 'pdf'],
        help="Supported formats: TXT, JSON, CSV, PDF"
    )

    if uploaded_file:
        try:
            # Process the uploaded file
            processed_data = process_file(uploaded_file)

            # Update session state with structured data and text content
            st.session_state.data_df = processed_data['data']
            st.session_state.text_content = processed_data['text']

            # Generate embeddings
            embeddings = generate_embeddings(st.session_state.text_content)

            # Update graph
            st.session_state.graph = graph_manager.update_graph(st.session_state.data_df)

            st.success("File processed successfully!")
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

# Main content
col1, col2 = st.columns(2)

# Left column - Knowledge Graph and Visualizations
with col1:
    st.header("Knowledge Graph")

    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["Graph View", "Table View", "Word Cloud View"])

    # Tab 1: Graph View
    with tab1:
        if len(st.session_state.graph.nodes()) > 0:
            # Get node positions using spring layout
            pos = nx.spring_layout(st.session_state.graph)

            # Create edges trace
            edge_x = []
            edge_y = []
            for edge in st.session_state.graph.edges():
                x0, y0 = pos[edge[0]]
                x1, y1 = pos[edge[1]]
                edge_x.extend([x0, x1, None])
                edge_y.extend([y0, y1, None])

            edges_trace = go.Scatter(
                x=edge_x, y=edge_y,
                line=dict(width=0.8, color='#888'),
                hoverinfo='none',
                mode='lines')

            # Create nodes trace
            node_x = []
            node_y = []
            node_text = []
            node_degrees = []
            for node in st.session_state.graph.nodes():
                x, y = pos[node]
                node_x.append(x)
                node_y.append(y)
                node_text.append(str(node))
                node_degrees.append(st.session_state.graph.degree(node))

            nodes_trace = go.Scatter(
                x=node_x, y=node_y,
                mode='markers+text',
                hoverinfo='text',
                text=node_text,
                textposition="bottom center",
                marker=dict(
                    showscale=True,
                    colorscale='viridis',
                    size=10,
                    color=node_degrees,
                    colorbar=dict(
                        thickness=15,
                        title=dict(
                            text='Node Connections',
                            side='right'
                        )
                    )
                )
            )

            # Create the figure
            fig = go.Figure(data=[edges_trace, nodes_trace],
                          layout=go.Layout(
                              showlegend=False,
                              hovermode='closest',
                              margin=dict(b=0, l=0, r=0, t=0),
                              xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                              yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                              plot_bgcolor='white'
                          ))

            # Add animation settings
            fig.update_layout(
                updatemenus=[{
                    'type': 'buttons',
                    'showactive': False,
                    'buttons': [{
                        'label': 'Play',
                        'method': 'animate',
                        'args': [None, {
                            'frame': {'duration': 500, 'redraw': True},
                            'fromcurrent': True,
                            'mode': 'immediate',
                            'transition': {'duration': 300}
                        }]
                    }]
                }]
            )

            # Display the interactive plot
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Upload data to visualize the knowledge graph")

    # Tab 2: Table View
    with tab2:
        if not st.session_state.data_df.empty:
            st.subheader("Structured Data")
            st.dataframe(st.session_state.data_df)
        else:
            st.info("Upload structured data (CSV/JSON) to view the table")

    # Tab 3: Word Cloud View
    with tab3:
        if st.session_state.text_content:
            # Generate word cloud
            wordcloud = WordCloud(width=800, height=400, 
                                background_color='white').generate(st.session_state.text_content)

            # Display word cloud
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
            plt.close()
        else:
            st.info("Upload text data to generate word cloud")

# Right column - Query interface
with col2:
    st.header("Query Interface")

    query = st.text_area("Enter your query:", height=100)

    if st.button("Execute Query"):
        if query:
            try:
                # Process query and get results
                results = query_processor.process_query(query, st.session_state.graph)

                # Display results
                st.subheader("Query Results")
                st.write(results)
            except Exception as e:
                st.error(f"Error processing query: {str(e)}")
        else:
            st.warning("Please enter a query")