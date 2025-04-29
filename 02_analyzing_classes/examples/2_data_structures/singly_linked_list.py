#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    """
    STATE (PROPERTIES):
    - value: any - The data stored in the node
    - next: Node | None - Reference to the next node
    """

    def __init__(self, value):
        """
        CONSTRUCTION:
        - value: comes directly from parameter
        - next: initialized to None
        """
        self.value = value
        self.next = None


class SinglyLinkedList:
    """
    STATE (PROPERTIES):
    - head: Node | None - Points to the first node in the list
    """

    def __init__(self):
        """
        CONSTRUCTION:
        - head: starts as None (empty list)
        """
        self.head = None

    def append(self, value):
        """
        BEHAVIOR (STATE-CHANGING):
        - Adds a new node to the end of the list

        DATA INTERACTION:
        - Modifies internal structure by linking nodes
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, value):
        """
        BEHAVIOR (STATE-CHANGING):
        - Removes the first node with a matching value

        Validation:
        - Does nothing if value not found

        DATA INTERACTION:
        - Modifies links between nodes
        """
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

