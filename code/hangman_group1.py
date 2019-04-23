import random
import os
import hangman_art as hang

def word_gen():
    with open ("english.txt", "r") as words:
        lines = words.read().split('\n')
    big_words = []
    for line in lines:
        if len(line) > 4:
            big_words.append(line)
    new_word = random.choice(big_words)
    return new_word

def blank_gen(new_word):
    blank_word = ""
    for char in new_word:
        blank_word = blank_word + "_"
    return blank_word


def check(new_word, blank_word, user, guesses):
    new_word = list(new_word)
    blank_word = list(blank_word)
    if user not in guesses:
        if user == '?':
            return 'question'
        else:
            guesses.append(user)
            if user in new_word:
                return 1
            elif user not in new_word:
                return 3
    elif user in guesses:
        return 2

    


def correct(new_word, blank_word, user):
    new_word = list(new_word)
    blank_word = blank_word.strip()
    blank_word = list(blank_word)
    for i in range(len(new_word)):
        if user == new_word[i]:
            blank_word[i] = user
    blank_word = "".join(blank_word)


    return blank_word

def incorrect(counter):
    counter -= 1
    return counter

def print_word(blank_word):
    for i in range(len(blank_word)):
        print(blank_word[i], end=' ')
    print('\n')

def random_letter(new_word, blank_word):
    user = random.choice(new_word)
    while user in blank_word:
        user = random.choice(new_word)
    return correct(new_word, blank_word, user)

def print_game(blank_word, guesses, counter):
    os.system('clear')
    for i in hang.header:
        print(i)
    if counter >= 8:
        for i in hang.man8:
            print(i)
    if counter == 7:
        for i in hang.man7:
            print(i)
    if counter == 6:
        for i in hang.man6:
            print(i)
    if counter == 5:
        for i in hang.man5:
            print(i)
    if counter == 4:
        for i in hang.man4:
            print(i)
    if counter == 3:
        for i in hang.man3:
            print(i)
    if counter == 2:
        for i in hang.man2:
            print(i)
    if counter == 1:
        for i in hang.man1:
            print(i)
    if counter == 0:
        for i in hang.man0:
            print(i)

    

    print(f"Letters already guessed: \n {guesses}")
    print_word(blank_word)
    print(f"Guesses remaining: {counter}")

def play():
    play_again = True
    while play_again:
        new_word = word_gen()
        blank_word = blank_gen(new_word)
        guesses = []
        counter = 10
<<<<<<< HEAD
        while counter >= 0:
=======
        print_game(blank_word, guesses, counter)
        while counter >= 0:
            check_user = 0
>>>>>>> 583794a8d6bb749e0006512aaeeaa6e5dde7feb9
            if new_word == blank_word:
                print("You won!")
                break
            elif counter ==0:
                print(f"You lose! The word was {new_word}")
                break
<<<<<<< HEAD
            user = input("guess a letter > ")
            # check(new_word, blank_word)
            if check(new_word, blank_word, user, guesses):
                blank_word = correct(new_word, blank_word, user)
                print_word(blank_word)
                print(f"Guesses remaining: {counter}")
            else:
                counter = incorrect(counter)
                print_word(blank_word)
                print(f"Guesses remaining: {counter}")
=======
            user = input("guess a letter > ").lower()
            check_user = check(new_word, blank_word, user, guesses)
            # check(new_word, blank_word)
            if check_user == 'question':
                blank_word = random_letter(new_word, blank_word)
                print_game(blank_word, guesses, counter)
                
            elif check_user == 3:
                counter = incorrect(counter)
                print_game(blank_word, guesses, counter)
                
            elif check_user == 2:
                print_game(blank_word, guesses, counter)
                
            elif check_user == 1:
                blank_word = correct(new_word, blank_word, user)
                print_game(blank_word, guesses, counter)
                
                
                
>>>>>>> 583794a8d6bb749e0006512aaeeaa6e5dde7feb9

        play_again = input("Would you like to play again? ")
        if play_again == "no":
            play_again = False


play()
