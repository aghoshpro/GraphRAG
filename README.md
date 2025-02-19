# GraphRAG

## Installation

### Clone Repository

- Create a working directory and navigate to it:

  ```bash
  cd ChatDocument
  ```

- Open `cmd` or `terminal` to clone repository

  ```bash
  git clone https://github.com/aghoshpro/ChatDocument.git
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
  pip install -r requirements.txt
  ```

- 🧪 Experiment with code if you want

  ```sh
  jupyter notebook
  ```

## Get API Keys

- Anthropic: <https://console.anthropic.com/settings/keys>
- OpenAI <https://platform.openai.com/settings/proj_D0EtqGQ3jNT0h8LnOHnLAVkO/api-keys>

- Put them in `.env` file and add it to `.gitignore` so it will be not shared during git commit
