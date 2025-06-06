# AIA

## Project Overview
This project aims to provide a local AI agent based on [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) with support for models served via [Ollama](https://ollama.ai/). The goal is to run an assistant on your own machine without relying on cloud APIs.

## Goals
- Offer a simple environment for experimenting with Open Interpreter
- Allow running agents completely offline with local models
- Keep configuration minimal and transparent

## Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai/) installed with at least one model

## Setup
1. Run the included setup script which creates `.venv`, installs requirements, copies `sitecustomize.py` and pulls the model specified by `OLLAMA_MODEL` if set:
   ```bash
   python setup_env.py
   ```
2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # on Windows use .venv\Scripts\activate
   ```
3. Copy `.env.example` to `.env` and add your `ANTHROPIC_API_KEY` if needed:
   ```bash
   cp .env.example .env
   ```
4. Verify the installation by running the smoke test:
   ```bash
   python test_smoke.py
   ```

## Configuration
- The agent reads a few environment variables when starting up:

- `OFFLINE` – controls whether only local models are used. It defaults to
  `true`, so the agent runs completely offline unless you explicitly set it to a
  falsey value.
- `ANTHROPIC_API_KEY` – when this variable is set, Open Interpreter can access
  Anthropics models online. Provide a valid key and set `OFFLINE=false` if you
  want to use cloud models.

## Temporary Patch for `Anthropic.__init__`
This repository includes a `sitecustomize.py` file that monkey‑patches
`Anthropic.__init__` to ignore the deprecated `proxies` parameter. Python will automatically import this module on startup as long as the file is located in the
project root or inside the active virtual environment. Until the upstream
`Anthropic` class is updated, keep this file in place so initialization succeeds
without extra configuration. When online, ensure your `ANTHROPIC_API_KEY`
environment variable is set before starting the agent.

## Running the Agent
After activating the virtual environment and installing requirements, start the
agent with:
```bash
python main.py
```
You can override the model or offline mode from the command line. For example:
```bash
python main.py --model ollama/phi3:mini
```
Pass `--offline` to force local-only mode regardless of the `OFFLINE` environment variable.
On Windows, you can use the provided batch script which activates the
virtual environment and launches the agent:
```bat
run_agent.bat
```
Before running, set `ANTHROPIC_API_KEY` if you want online model access
and `OFFLINE=true` to force local mode.
The agent can run offline using local models through Ollama or connect to online services if the required API keys are provided.

### Offline example
Run completely offline with a locally served model by setting `OFFLINE=true`:
```bash
OFFLINE=true python main.py
```
The agent defaults to offline mode, so this step is optional but ensures it won't
attempt any network calls. By default it uses the `ollama/llama3` model unless
you specify another. Set `OFFLINE=false` along with your API key to enable
cloud access.

### Online example
Provide your key to access Anthropic models via the cloud:
```bash
ANTHROPIC_API_KEY=<your-key> python main.py
```

### Windows quick start
Windows users can simply run the `run_agent.bat` script once the virtual environment is ready.

## License
This project is licensed under the [MIT License](LICENSE).
