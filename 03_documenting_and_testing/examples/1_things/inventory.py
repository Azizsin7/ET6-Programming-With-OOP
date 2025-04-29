#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Inventory:
    """A class to manage an inventory of items using a dictionary.

    Each item is stored as a key, with its quantity as the value.

    Example:
        >>> inv = Inventory()
        >>> inv.add("apple", 3)
        >>> inv.add("apple", 2)
        >>> inv.get("apple")
        5
    """

    def __init__(self):
        """Initialize an empty inventory."""
        self._items = {}

    def add(self, item: str, quantity: int = 1) -> None:
        """Add quantity of an item to the inventory.

        Args:
            item (str): The item name.
            quantity (int): Amount to add. Must be positive.

        Raises:
            ValueError: If quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self._items[item] = self._items.get(item, 0) + quantity

    def get(self, item: str) -> int:
        """Return the quantity of an item in the inventory.

        Args:
            item (str): Item to look up.

        Returns:
            int: Quantity (0 if not found).
        """
        return self._items.get(item, 0)

    def remove(self, item: str, quantity: int) -> None:
        """Remove a quantity of an item from the inventory.

        Raises:
            ValueError: If quantity is negative or exceeds stock.
        """
        if quantity < 0:
            raise ValueError("Cannot remove negative quantity.")
        if self._items.get(item, 0) < quantity:
            raise ValueError("Not enough stock.")
        self._items[item] -= quantity
        if self._items[item] == 0:
            del self._items[item]

    def list_items(self) -> dict[str, int]:
        """Return a copy of the inventory."""
        return self._items.copy()
