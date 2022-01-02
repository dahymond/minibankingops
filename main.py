# Class for BankAccount
class BankAccount:

    # The init method or constructor
    def __init__(self, initial_amount, currency):

        # Instance Variable
        self.currency = currency
        self.balance = initial_amount

    def deposit(self, amount):
        if amount < 0:
            return f"Sorry negative value ({amount}) not allowed"
        else:
            self.balance = self.balance + amount
            return f"Deposit of {self.currency} {amount} successful. Your new balance is {self.currency} {self.balance}"

    def withdraw(self, amount):
        if amount < 0:
            return f"Sorry negative value ({amount}) not allowed"
        elif self.balance >= amount:
            self.balance = self.balance - amount
            return f"Withdrawal successful. Your new balance is {self.currency} {self.balance}"
        else:
            return "Insufficient balance"

    def my_balance(self):
        return f"Your account balance is {self.balance}"


Rodger = BankAccount(100, "USD")
print(Rodger.my_balance())
print(Rodger.withdraw(-50))
print(Rodger.my_balance())


Edward = BankAccount(300, "USD")
print(Edward.my_balance())
print(Edward.withdraw(-50))
print(Edward.my_balance())
