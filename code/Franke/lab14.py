import random
def pick6():
    six_digits = [random.randint(1, 100) for _ in range(6)]
    return six_digits

Winning = pick6()
print(Winning)
def final_gain():
    Current_balance = 0
    pay = 0
    for _ in range(100000):
        Ticket = pick6()
        Matching = 0
        Wins = 0
        for i in range(len(Ticket)):
            if Winning[i] == Ticket[i]:
                        Matching += 1
        if  Matching == 1:
            Wins += 4
        elif Matching == 2:
            Wins += 7
        elif Matching == 3:
            Wins += 100
        elif  Matching == 4:
            Wins += 50000
        elif  Matching == 5:
            Wins += 1000000
        elif  Matching == 6:
            Wins += 25000000

        Current_balance -= 2
        pay = Current_balance + Wins
        ROI = pay/Current_balance
    return pay,ROI


print(final_gain())