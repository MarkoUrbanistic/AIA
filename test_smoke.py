"""Simple smoke test to verify Open Interpreter installation."""

from interpreter import interpreter

# Smoke test: import the interpreter package and confirm the object exists.
interpreter.offline = True
assert hasattr(interpreter, "chat")
print("Interpreter loaded. offline=%s" % interpreter.offline)
