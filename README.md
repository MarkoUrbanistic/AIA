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
1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify the installation by running the smoke test:
   ```bash
   python test_smoke.py
   ```

## Temporary Patch for `Anthropic.__init__`
This repository includes a `sitecustomize.py` file that monkey‑patches
`Anthropic.__init__` to ignore the deprecated `proxies` parameter. Python will
automatically import this module on startup as long as the file is located in the
project root or inside the active virtual environment. Until the upstream
`Anthropic` class is updated, keep this file in place so initialization succeeds
without extra configuration. When online, ensure your `ANTHROPIC_API_KEY`
environment variable is set before starting the agent.

## Running the Agent
After activating the virtual environment and installing requirements, start the agent with:
```bash
python main.py
```
The agent can run offline using local models through Ollama or connect to online services if the required API keys are provided.

### Offline example
Run completely offline with a locally served model by setting `OFFLINE=true`:
```bash
OFFLINE=true python main.py
```
By default the agent will use `ollama/llama3` if no other model is specified.

### Online example
Provide your key to access Anthropic models via the cloud:
```bash
ANTHROPIC_API_KEY=<your-key> python main.py
```

### Windows quick start
Windows users can simply run the `run_agent.bat` script once the virtual environment is ready.

## License
This project is licensed under the [MIT License](LICENSE).
