vq0ck5-codex/evaluate-pywinauto-or-uiautomation-for-automation
import importlib.util

# Basic sanity check that the interpreter package is installed.
assert importlib.util.find_spec("interpreter") is not None
print("interpreter module available")
=======
try:
    import openinterpreter  # type: ignore
except ModuleNotFoundError:
    import interpreter as openinterpreter

exit_code = 0

try:
    openinterpreter.OpenInterpreter().run('print("hello")')
    openinterpreter.OpenInterpreter().run("2+2", offline=True)
except Exception:
    exit_code = 1

raise SystemExit(exit_code)
main
