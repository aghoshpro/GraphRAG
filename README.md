# Knowledge Graph RAG

Knowledge Graph RAG is a special type of RAG system that combines the benefits of knowledge graphs with large language models (LLMs). In GraphRAG, the knowledge graph serves as an organised data structure of factual information, while the LLM functions as a reasoning engine, processing user questions, obtaining appropriate knowledge from the graph, and delivering logical responses.

Recent scientific research [[1](https://arxiv.org/abs/2405.02048), [2](https://arxiv.org/pdf/2404.16130)] reveals that GraphRAG outperforms vector store-powered traditional RAG systems with more accurate responses in a cost effective and scalable way.

<img src="assets\grapgragg.jpg">

Consider the following scenario to demonstrate GraphRAG's effectiveness: both a traditional RAG and GraphRAG are charged with identifying the top five themes in a dataset. The baseline RAG struggled to retrieve unrelated text and represent the essential themes accurately. In contrast, GraphRAG provided a concise and meaningful response, identifying the main ideas and supporting them with source material references.

## Traditional RAG vs GraphRAG

traditional RAG treats each document as an isolated unit, while graph RAG captures the relationships between entities mentioned in the documents. This structural understanding enables more sophisticated querying and better answers.

<img src="assets\Vs.png">

- Source: [Collab](https://colab.research.google.com/drive/1MnZ6CeUNiVTrJGwYpJaduQBbCsNEVrbD?usp=sharing#scrollTo=iXmdiUY7NlQA)

## Environment Setup

### 1. Clone Repository

- Create a working directory and navigate to it:

  ```bash
  cd GraphRAG
  ```

- Open `cmd` or `terminal` to clone repository

  ```bash
  git clone https://github.com/aghoshpro/GraphRAG.git
  ```

### 2. **Setup Local Environment**

- Create a virtual environment `myvenv` inside the `./GraphRAG` folder and activate it:

  ```bash
  python -m venv myvenv
  ```

  ```bash
  # Windows
  .\myvenv\Scripts\activate    # OR source myvenv/bin/activate (in Linux or Mac)
  ```

- Install dependencies:

  ```bash
  pip install --upgrade -r requirements.txt
  ```
<!-- ### Get API Keys

- Anthropic: <https://console.anthropic.com/settings/keys>
- OpenAI <https://platform.openai.com/settings/proj_D0EtqGQ3jNT0h8LnOHnLAVkO/api-keys>

- Put them in `.env` file and add it to `.gitignore` so it will be not shared during git commit -->

### 3. Start Neo4J Docker

  ```sh
  docker compose up
  ```

## 🕹️ Run

```bash
streamlit run app.py
```

- Select `llama3.2` as the model and start chatting.

### 🧪 OR Experiment with code if you want

  ```sh
  jupyter notebook
  ```

## References

1. [pip](https://pip.pypa.io/en/stable/installation/)
2. [PythonNotes](https://note.nkmk.me/en/)
3. [LangChain ChatModels](https://python.langchain.com/docs/integrations/chat/)
4. [LangChain Neo4J](https://neo4j.com/labs/genai-ecosystem/langchain/)
5. [LangChain Community](https://api.python.langchain.com/en/latest/community_api_reference.html)
6. [Langchain SQL](https://python.langchain.com/docs/how_to/sql_prompting/)

### Knowledge Graph

1. [Neo4J KG](https://neo4j.com/blog/genai/what-is-knowledge-graph/)
2. [RDFvsPropKG](https://neo4j.com/blog/knowledge-graph/rdf-vs-property-graphs-knowledge-graphs/)
3. [NLPGraph](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-020-00383-w/metrics)

### Graph RAG

1. [Kdnuggets](https://www.kdnuggets.com/an-introduction-to-graph-rag)
2. [OntoText](https://www.ontotext.com/blog/matching-skills-and-candidates-with-graph-rag/)
3. [falkordb](https://www.falkordb.com/blogs/what-is-graphrag/)
4. [PG Vector](https://supabase.com/blog/openai-embeddings-postgres-vector)

### Colab

1. [Colab](https://colab.research.google.com/drive/1MnZ6CeUNiVTrJGwYpJaduQBbCsNEVrbD?usp=sharing#scrollTo=iXmdiUY7NlQA)

<!-- To find all districts of Bolzano with an elevation between 510-520 meters, you can use the following SPARQL query:\n\n

```sparql
SELECT ?distName ?elevation WHERE {
  ?region rdfs:label ?distName .
  ?region geo:asWKT ?distWkt .
  FILTER (CONTAINS(?distWkt, 'Bolzano') AND CONTAINS(?distWkt,'510-520'))
}
```

\n\nThis query filters the districts where the elevation is between 510-520 meters and contains the label "Bolzano".' -->
