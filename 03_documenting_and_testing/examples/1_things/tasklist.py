#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TaskList:
    """A class to manage a list of tasks, each with a description and completion status.

    Tasks are stored in the order they were added. Each task is represented as a dictionary
    with two keys: 'description' (str) and 'done' (bool).

    Example:
        >>> tl = TaskList()
        >>> tl.add("Write tests")
        >>> tl.add("Refactor code")
        >>> tl.complete(0)
        >>> tl.get_pending()
        ['Refactor code']
    """

    def __init__(self):
        """Initialize an empty task list."""
        self._tasks = []

    def add(self, description: str) -> None:
        """Add a new task to the list.

        Args:
            description (str): Description of the task.

        Raises:
            ValueError: If description is empty or whitespace.
        """
        if not description.strip():
            raise ValueError("Task description must not be empty.")
        self._tasks.append({'description': description, 'done': False})

    def complete(self, index: int) -> None:
        """Mark a task as completed by its index.

        Args:
            index (int): Index of the task in the list.

        Raises:
            IndexError: If the index is out of bounds.
        """
        self._tasks[index]['done'] = True

    def get_pending(self) -> list[str]:
        """Return a list of task descriptions that are not yet completed."""
        return [t['description'] for t in self._tasks if not t['done']]

    def reset(self) -> None:
        """Clear all tasks from the list."""
        self._tasks = []

    def count(self) -> int:
        """Return the number of tasks in the list."""
        return len(self._tasks)
