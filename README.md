# GraphRAG

## Installation

### Clone Repository

- Create a working directory and navigate to it:

  ```bash
  cd ChatDocument
  ```

- Open `cmd` or `terminal` to clone repository

  ```bash
  git clone https://github.com/aghoshpro/GraphRAG.git
  ```

### Setup Local Environment

- Create a virtual environment `myvenv` and activate it:

  ```bash
  python -m venv myvenv
  ```

  ```bash
  .\myvenv\Scripts\activate    # On Windows

  # ---------------------- OR ---------------------- #

  source myvenv/bin/activate  # On Linux or Mac
  ```

- Install dependencies:

  ```bash
  pip install --upgrade -r requirements.txt
  ```

### Get API Keys

- Anthropic: <https://console.anthropic.com/settings/keys>
- OpenAI <https://platform.openai.com/settings/proj_D0EtqGQ3jNT0h8LnOHnLAVkO/api-keys>

- Put them in `.env` file and add it to `.gitignore` so it will be not shared during git commit

### Start Neo4J Docker

  ```sh
  docker compose up
  ```

### 🧪 Experiment with code if you want

  ```sh
  jupyter notebook
  ```

## References

1. [pip](https://pip.pypa.io/en/stable/installation/)
2. [PythonNotes](https://note.nkmk.me/en/)
3. [LangChain ChatModels](https://python.langchain.com/docs/integrations/chat/)
4. [LangChain Neo4J](https://neo4j.com/labs/genai-ecosystem/langchain/)
5. [LangChain Community](https://api.python.langchain.com/en/latest/community_api_reference.html)
