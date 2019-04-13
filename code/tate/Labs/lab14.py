'''
Lab 14: Pick6
'''
import random

def gen_6():
    return [random.randint(1,99) for n in range(6)]

winning_ticket = gen_6()


######
def play_game():
    balance = 0
    ticket_cost = 2
    times_played = 100000
    earnings = 0
    match1 = 0
    match2 = 0
    match3 = 0
    match4 = 0
    match5 = 0
    match6 = 0

    for n in range(times_played):


        balance -= ticket_cost
        my_ticket = gen_6()
        count_matches = 0

        for num in range(len(my_ticket)):
            if my_ticket[num] == winning_ticket[num]:
                count_matches += 1

        if count_matches == 1:
            balance += 4
            earnings += 4
            match1 += 1
        elif count_matches == 2:
            balance += 7
            earnings += 7
            match2 += 1
        elif count_matches == 3:
            balance += 100
            earnings += 100
            match3 += 1
        elif count_matches == 4:
            balance += 50000
            earnings += 50000
            match4 += 1
        elif count_matches == 5:
            balance += 1000000
            earnings += 1000000
            match5 += 1
        elif count_matches == 6 :
            balance += 25000000
            earnings += 25000000
            match6 += 1

        expenses= ticket_cost * times_played
        roi = (earnings - expenses) / expenses

    # return f'Balance : {balance}',f'1 matches : {match1}',f'2 matches : {match2}',f'3 matches : {match3}',f'4 matches : {match4}',f'5 matches : {match5}',f'6 matches : {match6}',f'ROI : {roi}'

    return (f'Earnings : {earnings}, Expenses : {expenses}, ROI : {roi}')

print(play_game())
