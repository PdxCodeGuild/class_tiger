import random
import os

def main():
    itterations = 200000
    balance = 0
    winnings = 0
    expenses = 0
    match_six = 0
    match_five = 0
    match_four = 0
    match_three = 0
    match_two = 0
    match_one = 0
    
    winning_num = generate_num()

    for x in range(itterations):
        balance -= 2
        expenses -=2
        user_number = generate_num()
        matching_numbers = check_matching(winning_num, user_number)
        if matching_numbers == 6:
            balance += 25000000
            winnings += 25000000
            match_six += 1
        elif matching_numbers == 5:
            balance += 1000000
            winnings += 1000000
            match_five += 1
        elif matching_numbers == 4:
            balance += 50000
            winnings += 50000
            match_four += 1
        elif matching_numbers == 3:
            balance += 100
            winnings += 100
            match_three += 1
        elif matching_numbers == 2:
            balance += 7
            winnings += 7
            match_two += 1
        elif matching_numbers == 1:
            balance += 4
            winnings += 4
            match_one += 1
        if itterations %(itterations/100) == 0:
            os.system('clear')
            print(f" Match 6: {match_six} \n Match 5: {match_five} \n Match 4: {match_four} \n Match 3: {match_three} \n Match 2: {match_two} \n Match 1: {match_one} \n")
    roi = (winnings - expenses)/expenses
    print(f"Here are your results. After {itterations} attempts you have a total winnings of {winnings}, total expenses of {expenses}, with remaining balance of {balance}. Your ROI is {roi}!")

    
    

def generate_num():
    generated_num = []
    for i in range(0, 6):
        generated_num.append(random.randint(1,100))
    return generated_num

def check_matching(win_num, nums):
    counter = 0
    i = 0
    for win in win_num:
        if win == nums[i]:
            counter += 1
        i += 1
    return counter

main()