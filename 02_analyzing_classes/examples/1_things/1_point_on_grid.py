#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Coordinates:
    """
    STATE (PROPERTIES):
    - x: int - The horizontal position coordinate
    - y: int - The vertical position coordinate

    Note: This class represents a simple 2D point with integer coordinates.
    """

    def __init__(self, _x: int = 0, _y: int = 0) -> None:
        """
        CONSTRUCTION (INITIALIZATION):
        - x: comes directly from _x parameter (defaults to 0)
        - y: comes directly from _y parameter (defaults to 0)

        Validation:
        - No explicit validation, assumes inputs are valid integers
        """
        self.x = _x
        self.y = _y

    def up(self, units: int = 0) -> None:
        """
        BEHAVIOR (STATE-CHANGING):
        - Increases y coordinate by units (moving up)

        Validation:
        - No explicit validation

        DATA INTERACTION:
        - Directly modifies internal state without feedback
        """
        self.y += units

    def down(self, units: int = 0) -> None:
        """
        BEHAVIOR (STATE-CHANGING):
        - Decreases y coordinate by units (moving down)

        Validation:
        - No explicit validation

        DATA INTERACTION:
        - Directly modifies internal state without feedback
        """
        self.y -= units

    def right(self, units: int = 0) -> None:
        """
        BEHAVIOR (STATE-CHANGING):
        - Increases x coordinate by units (moving right)

        Validation:
        - No explicit validation

        DATA INTERACTION:
        - Directly modifies internal state without feedback
        """
        self.x += units

    def left(self, units: int = 0) -> None:
        """
        BEHAVIOR (STATE-CHANGING):
        - Decreases x coordinate by units (moving left)

        Validation:
        - No explicit validation

        DATA INTERACTION:
        - Directly modifies internal state without feedback
        """
        self.x -= units
