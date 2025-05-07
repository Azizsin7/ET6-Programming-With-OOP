#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BankAccount:
    """
    STATE (PROPERTIES):
    - owner: str - Name of the account owner
    - balance: float - Current account balance (always >= 0)
    - transaction_history: list[str] - Record of all transactions
    - account_number: str - Unique identifier starting with "ACC"
    - is_active: bool - Whether the account can process transactions
    """
    
    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        """
        CONSTRUCTION (INITIALIZATION):
        - owner: comes directly from owner_name parameter
        - balance: comes from initial_balance parameter (defaults to 0.0)
        - transaction_history: hardcoded as an empty list
        - account_number: derived from owner_name using a calculation
        - is_active: hardcoded to True for all new accounts
        
        Validation:
        - No explicit validation, assumes inputs are valid
        """
        self.owner = owner_name
        self.balance = initial_balance
        self.transaction_history = []
        self.account_number = "ACC" + "".join([str(ord(c) % 10) for c in owner_name])
        self.is_active = True
    
    def deposit(self, amount: float) -> bool:
        """
        BEHAVIOR (STATE-CHANGING):
        - Increases balance by amount
        - Adds a transaction record to history
        
        Validation:
        - Only accepts positive amounts
        - Only works if account is active
        
        STATE ACCESS:
        - Returns success/failure as bool
        - Changes internal data but doesn't expose it directly

        RETURNS: success/failure as boolean value
        """
        if amount > 0 and self.is_active:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount: float) -> bool:
        """
        BEHAVIOR (STATE-CHANGING):
        - Decreases balance by amount
        - Adds a transaction record to history
        
        Validation:
        - Only accepts positive amounts
        - Only allows withdrawals up to current balance
        - Only works if account is active
        
        STATE ACCESS:
        - Changes internal data but doesn't expose it directly

        RETURNS: success/failure as boolean value
        """
        if self.is_active and 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def get_balance(self) -> float:
        """
        BEHAVIOR (INFORMATION-PROVIDING):
        - Provides current balance without changing it
        
        STATE ACCESS:
        - Gives read-only access to balance value
        - Preferred way to access balance rather than reading the property directly

        RETURNS: .balance
        """
        return self.balance

    def close_account(self) -> None:
        """
        BEHAVIOR (STATE-CHANGING):
        - Deactivates the account
        - Adds closure to transaction history
        
        STATE ACCESS:
        - No return value
        - Changes internal state but doesn't expose it
        """
        self.is_active = False
        self.transaction_history.append("Account closed")
