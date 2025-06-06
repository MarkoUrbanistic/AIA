@echo off
REM Activate virtual environment and run the agent
REM Set ANTHROPIC_API_KEY if you want to use online models
REM Set OFFLINE=true to force local mode
call .venv\Scripts\activate
python main.py
