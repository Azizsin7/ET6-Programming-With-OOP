#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from ..inventory import Inventory

class TestAdd(unittest.TestCase):
    """Unit tests for Inventory.add."""

    def test_add_new_item(self):
        """Adding a new item should create an entry with correct quantity."""
        inv = Inventory()
        inv.add("apple", 3)
        self.assertEqual(inv.get("apple"), 3)

    def test_add_existing_item_increments_quantity(self):
        """Adding an existing item should increase its quantity."""
        inv = Inventory()
        inv.add("apple", 2)
        inv.add("apple", 3)
        self.assertEqual(inv.get("apple"), 5)

    def test_add_negative_quantity_raises(self):
        """Adding a negative or zero quantity should raise ValueError."""
        inv = Inventory()
        with self.assertRaises(ValueError):
            inv.add("apple", 0)

class TestGet(unittest.TestCase):
    """Unit tests for Inventory.get."""

    def test_get_existing_item(self):
        """Get should return the correct quantity for known items."""
        inv = Inventory()
        inv.add("banana", 1)
        self.assertEqual(inv.get("banana"), 1)

    def test_get_unknown_item_returns_zero(self):
        """Get should return 0 for items not in inventory."""
        inv = Inventory()
        self.assertEqual(inv.get("unknown"), 0)

class TestRemove(unittest.TestCase):
    """Unit tests for Inventory.remove."""

    def test_remove_reduces_quantity(self):
        """Remove should reduce quantity correctly."""
        inv = Inventory()
        inv.add("apple", 5)
        inv.remove("apple", 3)
        self.assertEqual(inv.get("apple"), 2)

    def test_remove_entire_quantity_removes_item(self):
        """Removing all of an item's quantity should delete it from inventory."""
        inv = Inventory()
        inv.add("apple", 3)
        inv.remove("apple", 3)
        self.assertEqual(inv.get("apple"), 0)
        self.assertNotIn("apple", inv.list_items())

    def test_remove_too_much_raises(self):
        """Trying to remove more than available should raise ValueError."""
        inv = Inventory()
        inv.add("apple", 1)
        with self.assertRaises(ValueError):
            inv.remove("apple", 2)

    def test_remove_negative_raises(self):
        """Negative removal should raise ValueError."""
        inv = Inventory()
        inv.add("apple", 2)
        with self.assertRaises(ValueError):
            inv.remove("apple", -1)

class TestListItems(unittest.TestCase):
    """Unit tests for Inventory.list_items."""

    def test_list_returns_copy(self):
        """list_items should return a copy, not internal state."""
        inv = Inventory()
        inv.add("x", 1)
        items = inv.list_items()
        items["x"] = 999
        self.assertNotEqual(inv.get("x"), 999)

class TestInventoryIntegration(unittest.TestCase):
    """Integration tests for Inventory class."""

    def test_add_remove_get_sequence(self):
        """Simulate basic usage pattern: add, remove, get."""
        inv = Inventory()
        inv.add("pen", 10)
        inv.remove("pen", 4)
        inv.add("pen", 2)
        self.assertEqual(inv.get("pen"), 8)
