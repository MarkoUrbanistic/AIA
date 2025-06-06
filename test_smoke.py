import importlib.util

# Basic sanity check that the interpreter package is installed.
assert importlib.util.find_spec("interpreter") is not None
print("interpreter module available")
