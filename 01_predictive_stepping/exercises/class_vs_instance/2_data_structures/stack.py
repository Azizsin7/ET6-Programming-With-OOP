#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


# Create stacks of books
fiction = Stack()
nonfiction = Stack()

# add fiction books to the fiction stack
fiction.push("Pride and Prejudice")
fiction.push("Life of Pi")
fiction.push("Homecoming")

# add nonfiction books to the nonfiction stack
nonfiction.push("Land")
nonfiction.push("1491")
nonfiction.push("Encyclopedia Britannica")
nonfiction.push("Webster Dictionary")

# Take the top book from each stack
fiction.pop()  # Removes "Homecoming"
nonfiction.pop()  # Removes "Webster Dictionary"

# Check the top book on each stack
top_fiction = fiction.peek()
top_nonfiction = nonfiction.peek()

# Final state of the stacks
print("Top Fiction Books:", top_fiction)
print("All Fiction Books:", fiction.items)

print("Top Nonfiction Books:", top_nonfiction)
print("All Nonfiction Books:", nonfiction.items)
