class ATM:
    def __init__(self, name):
        self.balance = 0
        self.name = name
        self.check = False
        # self.action = ''
        self.transactions_list = []

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance =+ amount
        # self.action = "deposited"
        self.transactions_list.append(f"{self.name} deposited ${amount}")
        return amount

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.check = True
            return(self.check)
           
    def withdrawal(self, amount):
        if self.check_withdrawal(amount) == True:
            self.balance -= amount
            self.transactions_list.append(f"{self.name} withdrew ${amount}")
            return amount
        else:
            print( "- - not enough money - -")

    def print_transactions(self):
        for each in self.transactions_list:
            print(each)

    def repl(self):
        while True:
            x = input("What would you like to do? \ndeposit, withdraw, check balance, history, or done > ")
            if x == "deposit":
                amount = int(input("how much would you like to deposit? > "))
                self.deposit(amount)
            elif x == "withdraw":
                amount = int(input("how much would you like to withdraw? > "))
                self.withdrawal(amount)
            elif x == "check balance":
                self.check_balance()
            elif x == "history":
                self.print_transactions()
            elif x == "done":
                break
            else:
                print("Please try again")
# # name = account1
a1 = ATM("Account-1")
a1.repl()            
# a1.deposit(200)
# a1.withdrawal(50)
# # print(a1.check_withdrawal(100))
# a1.print_transactions()
