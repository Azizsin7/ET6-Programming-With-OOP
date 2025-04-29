#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Class declaration - a template for creating bank accounts
class BankAccount:

    # Initialization method - runs when a new instance is created
    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        # Instance variables - unique to each account
        self.owner = owner_name
        self.balance = initial_balance
        self.transaction_history = []

    # Instance methods - operations that can be performed on each account
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return True
        return False

    def get_statement(self) -> str:
        return f"Account for {self.owner}: Balance = ${self.balance}"


# Creating different instances of the BankAccount class
# Each instance has its own state (balance, owner, transaction history)
alice_account = BankAccount("Alice", 1000)  # Instance 1
bob_account = BankAccount("Bob", 500)  # Instance 2

# Operations on Alice's account
alice_account.deposit(250)
alice_account.withdraw(100)

# Operations on Bob's account
bob_account.deposit(1000)
bob_account.withdraw(300)

# Each instance maintains its own state
print(alice_account.get_statement())  # Should show $1150
print(bob_account.get_statement())  # Should show $1200
