class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def transfer(self, other_account, amount):
        # Q1: Fill in the condition that checks if withdrawal is possible
        if _________:  # What condition should go here?
            self.withdraw(amount)
            other_account.deposit(amount)
            return True
        return False

# Create accounts
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 500)

# Q2: After the following operations, what will alice_account.balance be? _____
alice_account.deposit(200)
alice_account.withdraw(150)
# Add your answer here

# Q3: How many transactions will be in alice_account.transactions? _____
assert len(alice_account.transactions) == 2, "Alice should have 2 transactions"

# Transfer money
alice_account.transfer(bob_account, 300)

# Q4: What will bob_account.balance be now? _____
assert bob_account.balance == 800, "Bob's balance should be 800 after the transfer"

# Q5: What will alice_account.balance be now? _____
assert alice_account.balance == 750, "Alice's balance should be 750 after the transfer"

# Q6: If we create a new account with the same values as Bob's, will it be the same object?
charlie_account = BankAccount("Charlie", 800)
# Are bob_account and charlie_account the same object? _____
assert bob_account is not charlie_account, "These are different objects despite same balance"

# Q7: What happens if we modify the class itself by adding a new method?
def apply_interest(self, rate):
    interest = self.balance * rate
    self.deposit(interest)
    self.transactions.append(f"Interest: +${interest}")

# Add the method to the class
BankAccount.apply_interest = apply_interest

# Q8: Can we call this method on existing instances? _____
alice_account.apply_interest(0.05)
# What will alice_account.balance be now? _____
assert alice_account.balance == 787.5, "Alice's balance should include interest"

# Q9: How many items will be in alice_account.transactions now? _____
assert len(alice_account.transactions) == 5, "Alice should have 5 transactions"
