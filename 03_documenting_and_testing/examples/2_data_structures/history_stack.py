#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class HistoryStack:
    """A stack structure to manage navigation history.

    Supports push and pop operations with error checking.

    Example:
        >>> stack = HistoryStack()
        >>> stack.push("home")
        >>> stack.push("about")
        >>> stack.pop()
        'about'
    """

    def __init__(self):
        """Initialize an empty history stack."""
        self._stack = []

    def push(self, page: str) -> None:
        """Add a page to the top of the stack."""
        self._stack.append(page)

    def pop(self) -> str:
        """Remove and return the last visited page.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self._stack:
            raise IndexError("No history to go back to.")
        return self._stack.pop()

    def peek(self) -> str:
        """Return the last page without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self._stack:
            raise IndexError("History is empty.")
        return self._stack[-1]

    def is_empty(self) -> bool:
        """Return True if the history is empty."""
        return not self._stack

    def clear(self) -> None:
        """Clear the history."""
        self._stack.clear()
