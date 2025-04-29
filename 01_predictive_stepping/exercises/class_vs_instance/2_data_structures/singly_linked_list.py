#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, value):
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

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# Create a new list
list_1 = SinglyLinkedList()

# Add nodes
list_1.append("First")
list_1.append("Second")
list_1.append("Third")

# Remove the second node
list_1.remove("Second")

# Check the state of the list
list_1.print_list()


# Create another new list
list_2 = SinglyLinkedList()

# Add nodes
list_2.append(1)
list_2.append(2)
list_2.append(3)

# Remove the second node
list_2.remove(3)

# Check the state of the list
list_2.print_list()



# Create yet another new list
list_3 = SinglyLinkedList()

# Add nodes
list_3.append('a')
list_3.append('b')
list_3.append('c')

# Remove the second node
list_3.remove('a')

# Check the state of the list
list_3.print_list()
