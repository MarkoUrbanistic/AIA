import os
vq0ck5-codex/evaluate-pywinauto-or-uiautomation-for-automation
import sys
import types
import argparse
main
from interpreter import interpreter
from interpreter.terminal_interface.start_terminal_interface import start_terminal_interface

# Inject a lightweight ComputerTool implementation based on pywinauto if
# the default one cannot be imported (e.g. missing pyautogui on Windows).
try:
    import interpreter.computer_use.tools.computer  # noqa: F401
except Exception:  # pragma: no cover - only executed when pyautogui is missing
    from windows_computer_tool import ComputerTool as WinComputerTool

    module = types.ModuleType("interpreter.computer_use.tools.computer")
    module.ComputerTool = WinComputerTool
    sys.modules["interpreter.computer_use.tools.computer"] = module


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run Open Interpreter")
    parser.add_argument(
        "--offline",
        help="Override OFFLINE environment variable (true/false)",
    )
    parser.add_argument(
        "--model",
        help="Specify model identifier (overrides MODEL environment variable)",
    )
    return parser.parse_args()


def configure_interpreter(args: argparse.Namespace) -> None:
    """Configure the default Open Interpreter instance."""
    # Determine offline mode (default True)
    offline_env = os.getenv("OFFLINE", "true")
    offline_value = args.offline if args.offline is not None else offline_env
    interpreter.offline = str(offline_value).lower() in {"1", "true", "yes"}

    # Determine model (from CLI, env var, or default Ollama model)
    model = args.model if args.model is not None else os.getenv("MODEL")
    if model:
        interpreter.llm.model = model

    # If running offline and no model selected, default to an Ollama model
    if interpreter.offline and not interpreter.llm.model:
        interpreter.llm.model = "ollama/llama3"

    # Propagate Anthropic API key if provided
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key:
        os.environ["ANTHROPIC_API_KEY"] = api_key
    else:
        os.environ.pop("ANTHROPIC_API_KEY", None)


def main() -> None:
    args = parse_args()
    configure_interpreter(args)
    start_terminal_interface(interpreter)


if __name__ == "__main__":
    main()
