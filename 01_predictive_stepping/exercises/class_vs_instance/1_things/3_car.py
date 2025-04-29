#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Class declaration - a blueprint for creating cars
class Car:
    # Special method that initializes a new Car instance
    def __init__(self, make: str, model: str, year: int, color: str = "black"):
        # Instance variables - unique to each car
        self.make = make
        self.model = model
        self.year = year
        self.color = color or "black"
        self.speed = 0
        self.engine_on = False
        self.mileage = 0
        self.status_log = []  # To track car operations
    
    # Instance methods - actions that can be performed on each car
    def start_engine(self) -> bool:
        if not self.engine_on:
            self.engine_on = True
            self.status_log.append("Engine started")
            return True
        return False
    
    def stop_engine(self) -> bool:
        if self.engine_on:
            self.engine_on = False
            self.speed = 0
            self.status_log.append("Engine stopped")
            return True
        return False
    
    def accelerate(self, amount: int) -> int:
        if self.engine_on:
            self.speed += amount
            self.status_log.append(f"Accelerated by {amount}. New speed: {self.speed}")
            return self.speed
        self.status_log.append("Failed to accelerate - engine is off")
        return self.speed
    
    def brake(self, amount: int) -> int:
        if self.speed > 0:
            self.speed = max(0, self.speed - amount)
            self.status_log.append(f"Braked by {amount}. New speed: {self.speed}")
        return self.speed
    
    def drive(self, distance: float) -> float:
        if self.engine_on and self.speed > 0:
            self.mileage += distance
            self.status_log.append(f"Drove {distance} miles")
            return distance
        self.status_log.append("Failed to drive - engine off or speed is 0")
        return 0.0
    
    def get_status(self) -> dict:
        """Return a dictionary with the current state of the car"""
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


# Creating multiple Car instances - each with its own state
hyundai = Car("Hyundai", "Ioniq", 2023, "red")  # Instance 1
toyota = Car("Toyota", "Camry", 2022, "blue") # Instance 2

# Each car instance has its own behavior
hyundai_started = hyundai.start_engine()  # Returns True
hyundai_speed = hyundai.accelerate(60)    # Returns 60
hyundai_distance = hyundai.drive(10)      # Returns 10.0

toyota_started = toyota.start_engine()    # Returns True
toyota_speed = toyota.accelerate(40)      # Returns 40
toyota_distance1 = toyota.drive(5)        # Returns 5.0
toyota_new_speed = toyota.brake(20)       # Returns 20
toyota_distance2 = toyota.drive(3)        # Returns 3.0

# We can check the car status at any point
hyundai_status = hyundai.get_status()
toyota_status = toyota.get_status()


# Each car maintains its own state
hyundai_final_mileage = hyundai.mileage
toyota_final_mileage = toyota.mileage
