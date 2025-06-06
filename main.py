import os
from interpreter import interpreter
from interpreter.terminal_interface.start_terminal_interface import start_terminal_interface


def configure_interpreter() -> None:
    """Configure the default Open Interpreter instance."""
    # Determine offline mode (default True)
    offline_env = os.getenv("OFFLINE", "true")
    interpreter.offline = offline_env.lower() in {"1", "true", "yes"}

    # If running offline, force a local model if none is configured or if the
    # current model points to a cloud service.
    if interpreter.offline:
        if not interpreter.llm.model or "/" not in interpreter.llm.model:
            interpreter.llm.model = "ollama/llama3"

    # Propagate Anthropic API key if provided
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key:
        os.environ["ANTHROPIC_API_KEY"] = api_key
    else:
        os.environ.pop("ANTHROPIC_API_KEY", None)


def main() -> None:
    configure_interpreter()
    start_terminal_interface(interpreter)


if __name__ == "__main__":
    main()
