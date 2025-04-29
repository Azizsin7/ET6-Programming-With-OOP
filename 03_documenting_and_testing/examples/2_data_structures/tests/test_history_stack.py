#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from ..history_stack import HistoryStack

class TestPush(unittest.TestCase):
    """Unit tests for HistoryStack.push."""

    def test_push_adds_to_stack(self):
        """Push should add item to the top of the stack."""
        hs = HistoryStack()
        hs.push("home")
        self.assertEqual(hs.peek(), "home")

class TestPop(unittest.TestCase):
    """Unit tests for HistoryStack.pop."""

    def test_pop_returns_and_removes_last(self):
        """Pop should return last pushed item and remove it."""
        hs = HistoryStack()
        hs.push("a")
        hs.push("b")
        self.assertEqual(hs.pop(), "b")
        self.assertEqual(hs.peek(), "a")

    def test_pop_empty_stack_raises(self):
        """Popping an empty stack should raise IndexError."""
        hs = HistoryStack()
        with self.assertRaises(IndexError):
            hs.pop()

class TestPeek(unittest.TestCase):
    """Unit tests for HistoryStack.peek."""

    def test_peek_returns_top_without_removing(self):
        """Peek should show last item without popping it."""
        hs = HistoryStack()
        hs.push("x")
        hs.peek()
        self.assertEqual(hs.peek(), "x")
        self.assertFalse(hs.is_empty())

    def test_peek_empty_stack_raises(self):
        """Peeking an empty stack should raise IndexError."""
        hs = HistoryStack()
        with self.assertRaises(IndexError):
            hs.peek()

class TestIsEmpty(unittest.TestCase):
    """Unit tests for HistoryStack.is_empty."""

    def test_stack_is_empty_initially(self):
        """A new stack should be empty."""
        hs = HistoryStack()
        self.assertTrue(hs.is_empty())

    def test_stack_not_empty_after_push(self):
        """Stack should report non-empty after push."""
        hs = HistoryStack()
        hs.push("y")
        self.assertFalse(hs.is_empty())

class TestClear(unittest.TestCase):
    """Unit tests for HistoryStack.clear."""

    def test_clear_empties_stack(self):
        """Clear should remove all items from the stack."""
        hs = HistoryStack()
        hs.push("x")
        hs.clear()
        self.assertTrue(hs.is_empty())

class TestHistoryStackIntegration(unittest.TestCase):
    """Integration tests for HistoryStack."""

    def test_push_pop_sequence(self):
        """Push and pop a sequence and check final state."""
        hs = HistoryStack()
        hs.push("a")
        hs.push("b")
        hs.pop()
        hs.pop()
        self.assertTrue(hs.is_empty())
