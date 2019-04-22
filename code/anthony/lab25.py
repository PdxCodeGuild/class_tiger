class Account:

    balance = 0

    def __init__(self):
        self.can_withdraw = False
        self.transactions = []
    
    def check_balance(self):
        print(f"Balance: {self.balance}")
    
    def deposit(self, ammount):
        self.balance += ammount
        self.transactions.append(f"user deposited ${ammount}, remaining balance ${self.balance}")

    def check_withdrawal(self, ammount):
        if self.balance - ammount < 0:
            return False
        return True
    
    def withdraw(self, ammount):
        self.can_withdraw = self.check_withdrawal(ammount)
        if self.can_withdraw:
            self.balance -= ammount
            self.transactions.append(f"user withdrew ${ammount}, remaining balance ${self.balance}")
    
    def print_transactions(self):
        for i in self.transactions:
            print(i)

def deposit_withdraw(prompt):
    try:
        user_input = int(input("How much would you like to " + prompt + '? '))
    except ValueError:
        print("Not a valid form of deposit, try again.")
    return user_input


def main():
    menu_options = ['deposit', 'withdraw', 'check balance', 'history', 'quit']
    my_account = Account()
    while True:
        user_input = input("What would you like to do (deposit, withdraw, check balance, history, quit)? ")
        while user_input not in menu_options:
            user_input = input("What would you like to do (deposit, withdraw, check balance, history, quit)? ")
        if user_input == 'deposit':
            user_input = deposit_withdraw('deposit')
            my_account.deposit(user_input)
        elif user_input == 'withdraw':
            user_input = deposit_withdraw('withdraw')
            my_account.withdraw(user_input)
        elif user_input == 'check balance':
            my_account.check_balance()
        elif user_input == 'history':
            my_account.print_transactions()
        else:
            print("Thank you for using the ATM")
            break

main()