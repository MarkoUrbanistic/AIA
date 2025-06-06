@echo off
REM Quick start script for the AIA agent on Windows

REM Activate virtual environment if it exists
if exist .venv\Scripts\activate (
    call .venv\Scripts\activate
)

python main.py
