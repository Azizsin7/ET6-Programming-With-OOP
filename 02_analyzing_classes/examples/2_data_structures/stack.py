#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Stack:
    """
    STATE (PROPERTIES):
    - items: list - The internal list used to store stack elements (LIFO order)
    """

    def __init__(self):
        """
        CONSTRUCTION (INITIALIZATION):
        - items: starts as an empty list

        Validation:
        - None required
        """
        self.items = []

    def push(self, item):
        """
        BEHAVIOR (STATE-CHANGING):
        - Adds an item to the top of the stack

        DATA INTERACTION:
        - Directly modifies internal list
        - No return value
        """
        self.items.append(item)

    def pop(self):
        """
        BEHAVIOR (STATE-CHANGING):
        - Removes and returns the top item

        Validation:
        - Only pops if stack is non-empty

        DATA INTERACTION:
        - Returns removed item or None
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """
        BEHAVIOR (INFORMATION-PROVIDING):
        - Returns the top item without removing it

        DATA INTERACTION:
        - Read-only access to top element
        """
        if self.items:
            return self.items[-1]
        return None

    def is_empty(self):
        """
        BEHAVIOR (INFORMATION-PROVIDING):
        - Checks if the stack is empty

        DATA INTERACTION:
        - Returns a boolean
        """
        return len(self.items) == 0
