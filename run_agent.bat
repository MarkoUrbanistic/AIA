@echo off
 tmnpki-codex/show-agent-start-with-offline=true-and-local-model
REM Quick start script for the AIA agent on Windows
REM Set ANTHROPIC_API_KEY if you want to use online models
REM Set OFFLINE=true to force local mode

REM Activate virtual environment if it exists
if exist .venv\Scripts\activate (
    call .venv\Scripts\activate
)

=======
REM Activate virtual environment and run the agent
REM Set ANTHROPIC_API_KEY if you want to use online models
REM Set OFFLINE=true to force local mode
call .venv\Scripts\activate
 main
python main.py
