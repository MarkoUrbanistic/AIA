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

## Temporary Patch for `Anthropic.__init__`
Until the upstream `Anthropic` class is updated, apply the patch provided in this repository to allow initialization without API keys when running offline. When online, ensure your `ANTHROPIC_API_KEY` environment variable is set before starting the agent.

## Running the Agent
After activating the virtual environment and installing requirements, start the agent with:
```bash
python main.py
```
The agent can run offline using local models through Ollama or connect to online services if the required API keys are provided.
