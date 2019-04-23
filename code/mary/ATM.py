#ATM.py

class Account:
    def __init__(self, balance = 0.0):
        self.balance = balance
        self.history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.history.append(f"User deposited ${amount}.")
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance>self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.history.append(f"User withdrew ${amount}.")
        return self.balance

    def print_transactions(self):
        return self.history
        
acc = Account()
def repl(acc):
    while True:
        user_input = input(f"What would you like to do: deposit, withdraw, check balance, check history or exit? " )
        if user_input == "deposit":
            user_amt = int(input("How much would you like to deposit? "))
            (acc.deposit(user_amt))
        elif user_input == "withdraw":
            user_amt = int(input("How much would you like to withdraw? "))
            (acc.withdraw(user_amt))
        elif user_input == "check balance":
            print(acc.check_balance())
        elif user_input == "check history":
            print(acc.print_transactions())
        elif user_input == "exit":
            break
repl(acc)
