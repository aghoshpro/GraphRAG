##############################
#####  IMPORT LIBRARIES  #####
##############################
import os
print(f"Current working directory -> {os.getcwd()}")
from dotenv import load_dotenv
load_dotenv()
from tqdm import tqdm
### Neo4j
from neo4j import GraphDatabase
from neo4j import  Driver

### Langchain
from langchain_neo4j import Neo4jGraph
from langchain_neo4j import Neo4jVector
from langchain_core.runnables import  RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, CSVLoader
from langchain_community.vectorstores.neo4j_vector import remove_lucene_chars

### ChatModels (https://python.langchain.com/docs/integrations/chat/)
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

### Embeddings
from langchain_ollama import OllamaEmbeddings
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_experimental.graph_transformers import LLMGraphTransformer

from yfiles_jupyter_graphs import GraphWidget
from pydantic import BaseModel, Field

### FUNCTION #1
def displayGraph():
    driver = GraphDatabase.driver(
        uri = os.environ["NEO4J_URI"],
        auth = (os.environ["NEO4J_USERNAME"],
                os.environ["NEO4J_PASSWORD"]))

    session = driver.session()
    widget = GraphWidget(graph=session.run("MATCH (s)-[r:!MENTIONS]->(t) RETURN s,r,t").graph())
    widget.node_label_mapping = 'id'
    return widget

### FUNCTION #2
def queryGraph(query):
    driver = GraphDatabase.driver(  
        uri = os.environ["NEO4J_URI"],
        auth = (os.environ["NEO4J_USERNAME"],
                os.environ["NEO4J_PASSWORD"]))

    session = driver.session()
    result = session.run(query)
    return result   


### GET DATA
print("\nGetting Data...........................................\n")
# loader = JSONLoader(file_path="data/sample_docs/sample.json")
loader1 = CSVLoader(file_path="data/sample_docs/sample.csv")
# loader = TextLoader(file_path="data/sample_docs/sample.txt")
docs = loader1.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=24)
document_chucks = text_splitter.split_documents(documents=docs)

### Initialize LLM
print("\nInitializing LLM.......................................\n")

llm_type = os.getenv("LLM_TYPE", "ollama")

if llm_type == "ollama":
    llm = ChatOllama(
        model="llama3.2", temperature=0)
elif llm_type == "openai":
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
else:
    llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0)

print("\nInitializing LLMGraphTransformer........................\n")

llm_transformer = LLMGraphTransformer(llm=llm)
graph_documents = llm_transformer.convert_to_graph_documents(document_chucks)

### Initialize Neo4j graph
print("\nInitializing Neo4J Graph................................\n")

graph = Neo4jGraph()

graph.add_graph_documents(
    graph_documents,
    baseEntityLabel=True,
    include_source=True
)

print("\n Display Graph..........................................\n")
# displayGraph()

print("\nVector Embeddings.......................................\n")
embeddings = OllamaEmbeddings(
    model="mxbai-embed-large",
)

vector_index = Neo4jVector.from_existing_graph(
    embeddings,
    search_type="hybrid",
    node_label="Document",
    text_node_properties=["text"],
    embedding_node_property="embedding"
)
vector_retriever = vector_index.as_retriever()

print("\nGraphDatabase Driver......................................\n")

# driver = GraphDatabase.driver(
#         uri = os.environ["NEO4J_URI"],
#         auth = (os.environ["NEO4J_USERNAME"],
#                 os.environ["NEO4J_PASSWORD"]))

# def create_fulltext_index(tx):
#     query = '''
#     CREATE FULLTEXT INDEX `fulltext_entity_id` 
#     FOR (n:__Entity__) 
#     ON EACH [n.id];
#     '''
#     tx.run(query)

# # Function to execute the query
# def create_index():
#     with driver.session() as session:
#         session.execute_write(create_fulltext_index)
#         print("Fulltext is indexed successfully.")

# # Call the function to create the index
# try:
#     create_index()
# except:
#     pass

# # Close the driver connection
# driver.close()

# print("\n Chaining .............................................\n")

# class Entities(BaseModel):
#     """Identifying information about entities."""

#     names: list[str] = Field(
#         ...,
#         description="All the person, organization, or business entities that "
#         "appear in the text",
#     )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are extracting organization and person entities from the text.",
#         ),
#         (
#             "human",
#             "Use the given format to extract information from the following "
#             "input: {question}",
#         ),
#     ]
# )

# entity_chain = llm.with_structured_output(Entities)