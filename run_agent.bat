@echo off
REM Quick start script for the AIA agent on Windows
REM Set ANTHROPIC_API_KEY if you want to use online models
REM Set OFFLINE=true to force local mode

REM Activate virtual environment if it exists
if exist .venv\Scripts\activate (
    call .venv\Scripts\activate
)

python main.py
