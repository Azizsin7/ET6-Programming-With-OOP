#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

class ShoppingCart:
    """
    STATE (PROPERTIES):
    - customer_id: str - Unique identifier for the customer
    - items: dict[str, int] - Maps item names to quantities
    - prices: dict[str, float] - Maps item names to their prices
    - discount_code: str or None - Applied discount code (or None if none applied)
    - checkout_complete: bool - Whether checkout has been completed
    - last_modified: datetime - Timestamp of last cart modification
    """
    
    def __init__(self, customer_id: str):
        """
        CONSTRUCTION (INITIALIZATION):
        - customer_id: comes directly from parameter
        - items: starts as an empty dictionary
        - prices: starts as an empty dictionary
        - discount_code: starts as None (no discount)
        - checkout_complete: hardcoded to False for new carts
        - last_modified: set to current time when cart is created
        
        Validation:
        - No explicit validation, assumes customer_id is valid
        """
        self.customer_id = customer_id
        self.items = {}         # item_name: quantity
        self.prices = {}        # item_name: price
        self.discount_code = None
        self.checkout_complete = False
        self.last_modified = datetime.datetime.now()
    
    def add_item(self, item_name: str, price: float, quantity: int = 1) -> bool:
        """
        BEHAVIOR (create or update):
        - Adds or updates an item in the cart
        - Records the item's price
        - Updates the last_modified timestamp
        
        Validation:
        - Prevents changes to cart after checkout
        - Assumes positive quantity and valid price
        
        DATA INTERACTION:
        - Changes internal state but doesn't expose it directly

        RETURNS: complete/incomplete as a boolean value
        """
        if self.checkout_complete:
            return False
            
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
            self.prices[item_name] = price
            
        self.last_modified = datetime.datetime.now()
        return True
    
    def remove_item(self, item_name: str, quantity: int = 1) -> bool:
        """
        BEHAVIOR (delete or update):
        - Reduces item quantity or removes item completely
        - Updates the last_modified timestamp
        
        Validation:
        - Prevents changes to cart after checkout
        - Checks if item exists before attempting removal
        
        DATA INTERACTION:
        - Changes internal state but doesn't expose it directly

        RETURNS: True if item was removed, False otherwise
        """
        if self.checkout_complete or item_name not in self.items:
            return False
            
        if self.items[item_name] <= quantity:
            del self.items[item_name]
            del self.prices[item_name]
        else:
            self.items[item_name] -= quantity
            
        self.last_modified = datetime.datetime.now()
        return True
    
    def apply_discount(self, code: str) -> bool:
        """
        BEHAVIOR (update):
        - Applies a discount code to the cart
        - Updates the last_modified timestamp
        
        Validation:
        - Prevents changes to cart after checkout
        - Checks if discount code is valid
        
        DATA INTERACTION:
        - Changes internal state but doesn't expose it directly

        RETURNS: True if discount was applied, False otherwise
        """
        if self.checkout_complete:
            return False
            
        valid_codes = ["SAVE10", "SPRING25", "SUMMER20"]
        if code in valid_codes:
            self.discount_code = code
            self.last_modified = datetime.datetime.now()
            return True
        return False
    
    def get_total(self) -> float:
        """
        BEHAVIOR (read):
        - Calculates total price of all items
        - Applies any discount if present
        
        DATA INTERACTION:
        - Performs computation without changing state
        - Doesn't expose internal state directly

        RETURNS: calculated total price
        """
        total = sum(self.items[item] * self.prices[item] for item in self.items)
        
        # Apply discount if one exists
        if self.discount_code == "SAVE10":
            total *= 0.9  # 10% off
        elif self.discount_code == "SPRING25":
            total *= 0.75  # 25% off
        elif self.discount_code == "SUMMER20":
            total *= 0.8  # 20% off
            
        return round(total, 2)
    
    def checkout(self) -> dict:
        """
        BEHAVIOR (update and read):
        - Marks the cart as complete/locked
        - Updates the last_modified timestamp
        
        Validation:
        - Prevents checkout if cart is empty
        - Prevents repeated checkout
        
        DATA INTERACTION:
        - Changes internal state and provides summary information

        RETURNS: a dictionary. either a human-readable summary, or 
        """
        if self.checkout_complete:
            return {"error": "Checkout already completed"}
            
        if not self.items:
            return {"error": "Cart is empty"}
            
        self.checkout_complete = True
        self.last_modified = datetime.datetime.now()
        
        return {
            "customer_id": self.customer_id,
            "items": dict(self.items),  # Copy to prevent modification
            "total": self.get_total(),
            "discount_applied": self.discount_code,
            "checkout_time": self.last_modified
        }
    
    def get_cart_summary(self) -> dict:
        """
        BEHAVIOR (read):
        - Creates a snapshot of the cart's current state
        
        DATA INTERACTION:
        - Returns a dictionary with cart information
        - Provides read-only access to cart state
        - Includes calculated totals
        """
        return {
            "customer_id": self.customer_id,
            "item_count": sum(self.items.values()),
            "unique_items": len(self.items),
            "subtotal": sum(self.items[item] * self.prices[item] for item in self.items),
            "total_with_discount": self.get_total(),
            "discount_code": self.discount_code,
            "is_checkout_complete": self.checkout_complete
        }
