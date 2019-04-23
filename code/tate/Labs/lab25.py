'''
Lab 25 : ATM
'''

import os

class ATM:
    def __init__(self,balance=0):
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')
        return self.balance

    def __check_withdrawal(self,amount):
        # returns true if the amount won't put the account into negative
        if amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self,amount):
        if self.__check_withdrawal(amount):
            self.balance -= amount
            self.transactions.append(f'User withdrew ${amount}')
        else:
            print("Insufficient funds")
        return self.balance

    def print_transactions(self):
        return self.transactions

def check_int(user_input):
    while True:
        try:
            return int(user_input)
        except ValueError:
            print('Invalid Input')
            user_input = input('Please provide an integer > ')

def repl_func(account):
    while True:
        os.system('clear')
        print('Choose: deposit, withdraw, check balance, history, quit')
        user_choice = input('What would you like to do? > ').lower()

        if user_choice == 'deposit':
            amount = input('How much would you like to deposit?  > ')
            amount = check_int(amount)
            account.deposit(amount)
        elif user_choice == 'withdraw':
            amount = input('How much would you like to withdraw?  > ')
            amount = check_int(amount)
            account.withdraw(amount)
        elif user_choice == 'check balance':
            print(f'This account balance is: {account.check_balance()}')
        elif user_choice == 'history':
            print(account.print_transactions())
        elif user_choice =='quit':
            print('Goodbye!')
            break
        else:
            print('Invalid input')

        continue_choice = input('\nPress any key to continue')

acc1 = ATM(0)

repl_func(acc1)
