#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# class declaration - find Coordinates in your debugger's memory
class Coordinates:
    # special method declaration - find __init__ in your debugger's memory
    def __init__(self, _x: int = 0, _y: int = 0) -> None:
        # where do you find self. properties in the debugger?
        self.x = _x
        self.y = _y

    # method declaration - find up in your debugger's memory
    def up(self, units: int = 0) -> None:
        self.y += units

    def down(self, units: int = 0) -> None:
        self.y -= units

    def right(self, units: int = 0) -> None:
        self.x += units

    def left(self, units: int = 0) -> None:
        self.x -= units


# --- initializing class instances with different state ---

# Where is point_1 stored in the debugger?  
# What properties does it have? Which properties are shared, which are not?
point_1 = Coordinates(0, 0)
# What properties are the same for point_1 & 2?  What properties are different?
point_2 = Coordinates(1, 1)


#  --- calling methods to modify instance state ---

# Watch how point_1's state changes with each method call
# Do properties in Coordinates change when calling methods on point_1?
# Do properties in point_2 change when calling methods on point_1?
point_1.up(2)
point_1.right(3)
point_1.down(0)

point_2.down(3)
point_2.right(2)
point_2.up(4)

# What is the final state for both point_1 and point_2?
