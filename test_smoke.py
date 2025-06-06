"""Simple smoke test to verify Open Interpreter installation."""

try:
    from interpreter import interpreter
except ModuleNotFoundError:
    import openinterpreter as interpreter  # type: ignore

# Smoke test: import the interpreter package and confirm the object exists.
interpreter.offline = True
assert hasattr(interpreter, "chat")
print(f"Interpreter loaded. offline={interpreter.offline}")
