# guess_the_number

import random

comp_num = random.randint(1,10)
#print(comp_num)

guess_count = 1

previous_guesses = [0]
while True:
    print(previous_guesses)

    user_guess = int(input("Guess the number! > "))
    previous_guesses.append(user_guess)

    if abs(previous_guesses[guess_count-1] - comp_num) > abs(user_guess - comp_num):
        print("You are getting closer!!!")
    elif abs(previous_guesses[guess_count-1] - comp_num) < abs(user_guess - comp_num):
        print("You are getting worse!!!")

    if user_guess == comp_num:
        print("You are correct, amazing!")
        break

    if user_guess < comp_num:
        print('Your guess was too low!')
        user_guess = int(input('Try again! > '))
        guess_count += 1
    elif user_guess > comp_num:
        print('Your guess was too high!')
        user_guess = int(input('Try again! > '))
        guess_count += 1

    if guess_count > 10:
        print("You guessed too many times, you lose!")
        break



print("you guessed " + str(guess_count) + " times!")
