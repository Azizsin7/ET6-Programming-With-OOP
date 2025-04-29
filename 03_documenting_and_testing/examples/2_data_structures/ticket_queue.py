#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

class TicketQueue:
    """A queue for managing customer service tickets.

    New tickets are added to the back; service proceeds from the front.

    Example:
        >>> q = TicketQueue()
        >>> q.enqueue("Alice")
        >>> q.enqueue("Bob")
        >>> q.dequeue()
        'Alice'
    """

    def __init__(self):
        """Initialize an empty ticket queue."""
        self._queue = deque()

    def enqueue(self, name: str) -> None:
        """Add a new ticket to the back of the queue."""
        self._queue.append(name)

    def dequeue(self) -> str:
        """Remove and return the next ticket in line.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self._queue:
            raise IndexError("No tickets in queue.")
        return self._queue.popleft()

    def peek(self) -> str:
        """Return the next ticket without removing it."""
        if not self._queue:
            raise IndexError("Queue is empty.")
        return self._queue[0]

    def is_empty(self) -> bool:
        """Return True if the queue is empty."""
        return not self._queue

    def size(self) -> int:
        """Return the number of tickets in queue."""
        return len(self._queue)
