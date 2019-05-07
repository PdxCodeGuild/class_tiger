

import random

def pick6(pick6):
    pick6 = [random.randint(0, 100) for x in range(0, 7)]
    balance = 0
    winnings = 0
    for i in range(100001):
        balance -= 2
        tick6 = [random.randint(0, 100) for x in range(0, 7)]
        six = [x for x in range(0,7)]
        the_pick = dict(zip(six, pick6))
        the_tick = dict(zip(six, tick6))
        matches = 0   
        if the_pick[0] == the_tick[0]:
            matches += 1
        elif the_pick[1] == the_tick[1]:
            matches += 1
        elif the_pick[2] == the_tick[2]:
            matches += 1
        elif the_pick[3] == the_tick[3]:
            matches += 1    
            # return the_pick, the_tick
        elif the_pick[4] == the_tick[4]:
            matches += 1
        elif the_pick[5] == the_tick[5]:
            matches += 1
        elif the_pick[6] == the_tick[6]:
            matches += 1
        match_winnings = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
        winnings += (match_winnings[matches])
    print(f"ROI: {(winnings - abs(balance))/abs(balance) *100} %")
    print(f"Total Winnings: {winnings}")
    print(f"Total Expenses: {balance}")
    return (f'Final Balance: {winnings - abs(balance)}')
print(pick6(pick6))