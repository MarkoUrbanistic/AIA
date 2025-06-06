"""Simplified ComputerTool replacement using pywinauto.

This module provides a minimal subset of the Open Interpreter
ComputerTool functionality for sending mouse clicks and keystrokes.
It relies on pywinauto which works reliably on Windows.
"""
from __future__ import annotations

from typing import Tuple

try:
    from pywinauto.keyboard import send_keys
    from pywinauto import mouse
except Exception as exc:  # pragma: no cover - only executed on Windows
    raise ImportError(
        "pywinauto is required for windows_computer_tool"  # pragma: no cover
    ) from exc


class ComputerTool:
    """Very small subset of Open Interpreter's ComputerTool."""

    name = "computer"
    api_type = "computer_20241022"

    def __call__(self, *, action: str, text: str | None = None, coordinate: Tuple[int, int] | None = None, **_: object):
        """Execute a keyboard or mouse action."""
        if action in {"key", "type"}:
            if text is None:
                raise ValueError("text is required for key/type actions")
            send_keys(text, with_spaces=True)
        elif action in {"left_click", "right_click"}:
            if coordinate is None:
                raise ValueError("coordinate required for mouse click")
            x, y = coordinate
            button = "left" if action == "left_click" else "right"
            mouse.click(button=button, coords=(x, y))
        else:
            raise ValueError(f"Unsupported action: {action}")
        return {"status": "ok"}
