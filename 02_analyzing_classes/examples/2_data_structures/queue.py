#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Queue:
    """
    STATE (PROPERTIES):
    - items: list - The internal list used to store queue elements (FIFO order)
    """

    def __init__(self):
        """
        CONSTRUCTION (INITIALIZATION):
        - items: starts as an empty list

        Validation:
        - None required
        """
        self.items = []

    def enqueue(self, item):
        """
        BEHAVIOR (STATE-CHANGING):
        - Adds an item to the end of the queue

        DATA INTERACTION:
        - Directly modifies internal list
        """
        self.items.append(item)

    def dequeue(self):
        """
        BEHAVIOR (STATE-CHANGING):
        - Removes and returns the front item

        Validation:
        - Only dequeues if queue is non-empty

        DATA INTERACTION:
        - Returns removed item or None
        """
        if self.items:
            return self.items.pop(0)
        return None

    def peek(self):
        """
        BEHAVIOR (INFORMATION-PROVIDING):
        - Returns the front item without removing it

        DATA INTERACTION:
        - Read-only access to front element
        """
        if self.items:
            return self.items[0]
        return None

    def is_empty(self):
        """
        BEHAVIOR (INFORMATION-PROVIDING):
        - Checks if the queue is empty

        DATA INTERACTION:
        - Returns a boolean
        """
        return len(self.items) == 0
