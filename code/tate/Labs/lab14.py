'''
Lab 14: Pick6
'''
import random

def gen_6():
    return [random.randint(1,30) for n in range(6)]

winning_ticket = gen_6()

######
def play_game():
    balance = 0
    for n in range(10000):
        balance -= 2
        my_ticket = gen_6()
        count_matches = 0

        for num in range(len(my_ticket)):
            if my_ticket[num] == winning_ticket[num]:
                count_matches += 1

        if count_matches == 1:
            balance += 4
            print(balance, ' 4')
        elif count_matches == 2:
            balance += 7
            print(balance, ' 7')
        elif count_matches == 3:
            balance += 100
            print(balance, ' 100')
        elif count_matches == 4:
            balance += 50000
            print(balance, ' 50000')
        elif count_matches == 5:
            balance += 1000000
            print(balance, ' 100000')
        elif count_matches == 6 :
            balance += 25000000
            print(balance, ' 25000000')

    return balance

print(play_game())
