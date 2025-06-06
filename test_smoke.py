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
