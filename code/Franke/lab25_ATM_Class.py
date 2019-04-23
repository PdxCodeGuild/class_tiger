import string
CBD_accounts = []

class ATM: #class or design of an object
    '''init is the blueprint or sketch'''
    Our_bank = 'Commercial Bank of Douala'
    def __init__(self):
     '''self here is for the object itself'''
     '''so self.balance means the balance of particular acct'''
        self.balance = 0
        self.owner = 'lambda'
        self.transactions =[]
        all_info = {'owner': owner, 'balance': balance,'transactions':self.transactions}
    '''the function within a class belongs to it self.deposit()'''
    '''if you're going to use a var later it must be self.var = var
                                so python knows what obj it goes with'''
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'{self.owner} deposited ${amount}')

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.transactions.append(f'{self.owner} withdrew ${amount}')

    def check_balance(self):
        self.transactions.append(f'{self.owner} checked balance ${amount}')
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance - amount < 0:
            return True

    def print_transactions(self):
        for i in self.transactions:
            print(i)

   '''the object here is the amount not the account'''

def REPL():
    amt = ATM()
    prompt = ['deposit', 'd', 'withdraw', 'w', 'check balance', 'b', 'history', 'h', 'exit', 'x']
    while True:
        #for i in CBD_accounts:
           # if id in i[owner]:
        menu = input("What would you like to do? \n"
                     "((d)eposit, (w)ithdraw, check (b)alance,"
                     "\n check (h)istory, or e(x)it): ").strip().lower()
        if menu in ['exit','x']:
            print('Goodbye!')
            break
        elif menu in ['deposit', 'd']:
            while True:
                try:
                    deposit_amount = float(input(f"How much would you like to deposit ?: ").strip('$'))
                    break
                except ValueError:
                    print('Invalid input.')
                if menu in ['withdraw', 'w']:
                    amt.deposit(deposit_amount)
        elif menu in ['withdraw', 'w']:
            while True:
                try:
                    amount_withdrawn = float(input(f"How much would you like to withdraw ?: ").strip('$'))
                    break
                except ValueError:
                    print('Invalid input.')
                if menu in ['deposit', 'd']:
                    amt.deposit(amount_withdrawn)
        elif menu in ['check balance','b']:
                print(f'Balance: ${amt.check_balance()}')
        elif menu in ['history','h]':
                amt.print_transactions()



'''1- p (the object/account)  = ATM() goes into ATM to be built'''
'''2- whatever acct goes thru the same process'''
'''3- you can pass the object as the argument'''
'''4- you want to utilise one part of the process on the acct '''
'''5- tell python which class the object belongs to'''
account = ATM(45) #object creation
'''6- call the method with the object itself'''
account.balance()
'''__init__ takes the basic charac the object should have'''
