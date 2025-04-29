#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from ..tasklist import TaskList

class TestAdd(unittest.TestCase):
    """Unit tests for the TaskList.add method."""

    def test_add_valid_task_increases_count(self):
        """Adding a task should increase task count."""
        tl = TaskList()
        tl.add("Task 1")
        self.assertEqual(tl.count(), 1)

    def test_add_multiple_tasks_preserves_order(self):
        """Tasks should be stored in the order they were added."""
        tl = TaskList()
        tl.add("A")
        tl.add("B")
        self.assertEqual(tl._tasks[0]['description'], "A")
        self.assertEqual(tl._tasks[1]['description'], "B")

    def test_add_empty_description_raises(self):
        """Adding an empty or whitespace-only description should raise ValueError."""
        tl = TaskList()
        with self.assertRaises(ValueError):
            tl.add("   ")

class TestComplete(unittest.TestCase):
    """Unit tests for the TaskList.complete method."""

    def test_complete_sets_done_to_true(self):
        """Completing a task should set its 'done' field to True."""
        tl = TaskList()
        tl.add("Task")
        tl.complete(0)
        self.assertTrue(tl._tasks[0]['done'])

    def test_complete_invalid_index_raises(self):
        """Completing a nonexistent task should raise IndexError."""
        tl = TaskList()
        with self.assertRaises(IndexError):
            tl.complete(0)

class TestGetPending(unittest.TestCase):
    """Unit tests for the TaskList.get_pending method."""

    def test_get_pending_returns_all_tasks_by_default(self):
        """All added tasks should be pending by default."""
        tl = TaskList()
        tl.add("A")
        tl.add("B")
        self.assertEqual(tl.get_pending(), ["A", "B"])

    def test_get_pending_excludes_completed_tasks(self):
        """Completed tasks should not be included in the pending list."""
        tl = TaskList()
        tl.add("A")
        tl.add("B")
        tl.complete(0)
        self.assertEqual(tl.get_pending(), ["B"])

class TestReset(unittest.TestCase):
    """Unit tests for the TaskList.reset method."""

    def test_reset_clears_all_tasks(self):
        """Resetting should clear all tasks and set count to 0."""
        tl = TaskList()
        tl.add("A")
        tl.reset()
        self.assertEqual(tl.count(), 0)
        self.assertEqual(tl.get_pending(), [])

class TestCount(unittest.TestCase):
    """Unit tests for the TaskList.count method."""

    def test_count_matches_number_of_tasks(self):
        """Count should return the number of tasks, regardless of status."""
        tl = TaskList()
        tl.add("A")
        tl.add("B")
        self.assertEqual(tl.count(), 2)

class TestTaskListIntegration(unittest.TestCase):
    """Integration tests for typical workflows with TaskList."""

    def test_add_complete_pending_workflow(self):
        """Add several tasks, complete one, check pending list reflects state."""
        tl = TaskList()
        tl.add("A")
        tl.add("B")
        tl.add("C")
        tl.complete(1)
        self.assertEqual(tl.get_pending(), ["A", "C"])

    def test_reset_then_reuse(self):
        """TaskList should be reusable after reset."""
        tl = TaskList()
        tl.add("First round")
        tl.reset()
        tl.add("Second round")
        self.assertEqual(tl.count(), 1)
        self.assertEqual(tl.get_pending(), ["Second round"])
