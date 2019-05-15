#pick_6.py
import random
win_nums = []
user_nums = []
def pick6(win_nums):
    for i in range(0,6):
        x = random.randint(1, 99)
        win_nums.append(x)
    return(win_nums)
winning = pick6(win_nums)


def user6(user_nums):
    for i in range(0,6):
        y = random.randint(1,99)
        user_nums.append(y)
    return(user_nums)
ticket = pick6(user_nums)

def match_nums():
    payout =[0,4,7,100,50000,100000,25000000]
    matches=0
    for i in range(len(ticket)):
        if winning[i]==ticket[i]:
            matches +=1
    return payout[matches]



def buy_ticket():
    winning = pick6(win_nums)
    ticket = pick6(user_nums)
    current_bal = 0
    for i in range(100000):
        current_bal = current_bal -  2
        current_bal = current_bal + match_nums()
    return(current_bal)


earnings = match_nums()
expenses = buy_ticket()
ROI = (earnings - expenses)/expenses
print(earnings)
print(expenses)
print(ROI)
