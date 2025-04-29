#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

class ShoppingCart:
    def __init__(self, customer_id: str):
        import datetime
        self.customer_id = customer_id
        self.items = {}         # item_name: quantity
        self.prices = {}        # item_name: price
        self.discount_code = None
        self.checkout_complete = False
        self.last_modified = datetime.datetime.now()
    
    def add_item(self, item_name: str, price: float, quantity: int = 1) -> bool:
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
        if self.checkout_complete:
            return False
            
        valid_codes = ["SAVE10", "SPRING25", "SUMMER20"]
        if code in valid_codes:
            self.discount_code = code
            self.last_modified = datetime.datetime.now()
            return True
        return False
    
    def get_total(self) -> float:
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
        return {
            "customer_id": self.customer_id,
            "item_count": sum(self.items.values()),
            "unique_items": len(self.items),
            "subtotal": sum(self.items[item] * self.prices[item] for item in self.items),
            "total_with_discount": self.get_total(),
            "discount_code": self.discount_code,
            "is_checkout_complete": self.checkout_complete
        }

# --- practice writing some use cases ---
