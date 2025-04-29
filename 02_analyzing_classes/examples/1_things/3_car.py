#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Car:
    """
    STATE (PROPERTIES):
    - make: str - Manufacturer of the car
    - model: str - Model name of the car
    - year: int - Manufacturing year
    - color: str - Color of the car
    - speed: int - Current speed (always >= 0)
    - engine_on: bool - Whether the engine is running
    - mileage: float - Total distance the car has driven
    - status_log: list[str] - Record of all car operations
    """
    
    def __init__(self, make: str, model: str, year: int, color: str = "black"):
        """
        CONSTRUCTION (INITIALIZATION):
        - make, model, year: come directly from parameters
        - color: comes from parameter (defaults to "black")
        - speed: hardcoded to 0 for new cars
        - engine_on: hardcoded to False (engine off) for new cars
        - mileage: hardcoded to 0 for new cars
        - status_log: starts as an empty list
        
        Validation:
        - No explicit validation, assumes inputs are valid
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.engine_on = False
        self.mileage = 0
        self.status_log = [] 
    
    def start_engine(self) -> bool:
        """
        BEHAVIOR (STATE-CHANGING):
        - Changes engine_on to True
        - Adds a record to status_log
        
        Validation:
        - Only works if engine is currently off
        
        DATA INTERACTION:
        - Changes internal state but doesn't expose it directly

        RETURNS: success/failure as boolean value
        """
        if not self.engine_on:
            self.engine_on = True
            self.status_log.append("Engine started")
            return True
        return False
    
    def stop_engine(self) -> bool:
        """
        BEHAVIOR (STATE-CHANGING):
        - Changes engine_on to False
        - Resets speed to 0
        - Adds a record to status_log
        
        Validation:
        - Only works if engine is currently on
        
        DATA INTERACTION:
        - Changes internal state but doesn't expose it directly

        RETURNS: success/failure as boolean value
        """
        if self.engine_on:
            self.engine_on = False
            self.speed = 0
            self.status_log.append("Engine stopped")
            return True
        return False
    
    def accelerate(self, amount: int) -> int:
        """
        BEHAVIOR (STATE-CHANGING):
        - Increases speed by amount
        - Adds a record to status_log
        
        Validation:
        - Only works if engine is on
        
        DATA INTERACTION:
        - Returns the new speed value
        - Changes internal state and provides the new value
        """
        if self.engine_on:
            self.speed += amount
            self.status_log.append(f"Accelerated by {amount}. New speed: {self.speed}")
            return self.speed
        self.status_log.append("Failed to accelerate - engine is off")
        return self.speed
    
    def brake(self, amount: int) -> int:
        """
        BEHAVIOR (STATE-CHANGING):
        - Decreases speed by amount (never below 0)
        - Adds a record to status_log
        
        Validation:
        - Only has an effect if speed is greater than 0
        
        DATA INTERACTION:
        - Returns the new speed value
        - Changes internal state and provides the new value

        RETURNS: .speed
        """
        if self.speed > 0:
            self.speed = max(0, self.speed - amount)
            self.status_log.append(f"Braked by {amount}. New speed: {self.speed}")
        return self.speed
    
    def drive(self, distance: float) -> float:
        """
        BEHAVIOR (STATE-CHANGING):
        - Increases mileage by distance
        - Adds a record to status_log
        
        Validation:
        - Only works if engine is on AND speed is greater than 0
        
        DATA INTERACTION:
        - Changes internal state but doesn't expose it directly

        RETURNS: .distance if engine is on & running, or 0.0
        """
        if self.engine_on and self.speed > 0:
            self.mileage += distance
            self.status_log.append(f"Drove {distance} miles")
            return distance
        self.status_log.append("Failed to drive - engine off or speed is 0")
        return 0.0
    
    def get_status(self) -> dict:
        """
        BEHAVIOR (INFORMATION-PROVIDING):
        - Creates a snapshot of the car's current state
        
        DATA INTERACTION:
        - Provides read-only access to internal state
        - Formats last_action specially to show the most recent log entry

        RETURNS: a dictionary with all important instance properties
        """
        return {
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "engine_on": self.engine_on,
            "speed": self.speed,
            "mileage": self.mileage,
            "last_action": self.status_log[-1] if self.status_log else "No actions yet"
        }
    