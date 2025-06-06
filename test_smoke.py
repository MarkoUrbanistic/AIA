"""Basic smoke test to verify that Open Interpreter imports correctly."""

import os

os.environ.setdefault("OFFLINE", "true")

from main import configure_interpreter
from interpreter import OpenInterpreter

configure_interpreter()
OpenInterpreter().chat('print("hello")')
