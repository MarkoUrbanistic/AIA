"""Basic smoke test to verify that Open Interpreter imports correctly."""

import os
from argparse import Namespace

os.environ.setdefault("OFFLINE", "true")

from interpreter import interpreter
from main import configure_interpreter

configure_interpreter(Namespace(offline=None, model=None))
interpreter.chat('print("hello")')
