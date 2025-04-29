#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from ..ticket_queue import TicketQueue

class TestEnqueue(unittest.TestCase):
    """Unit tests for TicketQueue.enqueue."""

    def test_enqueue_adds_to_back(self):
        """New ticket should go to the end of the queue."""
        tq = TicketQueue()
        tq.enqueue("Alice")
        tq.enqueue("Bob")
        self.assertEqual(tq.peek(), "Alice")

class TestDequeue(unittest.TestCase):
    """Unit tests for TicketQueue.dequeue."""

    def test_dequeue_returns_front_item(self):
        """Dequeue should return and remove the front ticket."""
        tq = TicketQueue()
        tq.enqueue("A")
        tq.enqueue("B")
        self.assertEqual(tq.dequeue(), "A")
        self.assertEqual(tq.peek(), "B")

    def test_dequeue_empty_queue_raises(self):
        """Dequeuing an empty queue should raise IndexError."""
        tq = TicketQueue()
        with self.assertRaises(IndexError):
            tq.dequeue()

class TestPeek(unittest.TestCase):
    """Unit tests for TicketQueue.peek."""

    def test_peek_shows_front_without_removing(self):
        """Peek should return the front ticket without removing it."""
        tq = TicketQueue()
        tq.enqueue("Z")
        self.assertEqual(tq.peek(), "Z")
        self.assertEqual(tq.size(), 1)

    def test_peek_empty_queue_raises(self):
        """Peeking an empty queue should raise IndexError."""
        tq = TicketQueue()
        with self.assertRaises(IndexError):
            tq.peek()

class TestIsEmpty(unittest.TestCase):
    """Unit tests for TicketQueue.is_empty."""

    def test_empty_on_init(self):
        """Queue should be empty at initialization."""
        tq = TicketQueue()
        self.assertTrue(tq.is_empty())

    def test_not_empty_after_enqueue(self):
        """Queue should not be empty after adding items."""
        tq = TicketQueue()
        tq.enqueue("X")
        self.assertFalse(tq.is_empty())

class TestSize(unittest.TestCase):
    """Unit tests for TicketQueue.size."""

    def test_size_reflects_queue_length(self):
        """Size should match the number of enqueued items."""
        tq = TicketQueue()
        self.assertEqual(tq.size(), 0)
        tq.enqueue("A")
        tq.enqueue("B")
        self.assertEqual(tq.size(), 2)

class TestTicketQueueIntegration(unittest.TestCase):
    """Integration tests for TicketQueue."""

    def test_enqueue_dequeue_sequence(self):
        """Simulate real-world usage: enqueue, dequeue, repeat."""
        tq = TicketQueue()
        tq.enqueue("T1")
        tq.enqueue("T2")
        tq.dequeue()
        tq.enqueue("T3")
        self.assertEqual(tq.peek(), "T2")
