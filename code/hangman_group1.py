with open ("english.txt", "r") as words:
    lines = words.read().split('\n')

big_words = []
for line in lines:
    if len(line) > 4:
        big_words.append(line)

import random
# from string import join
new_word = random.choice(big_words)
blank_word = ""
for char in new_word:
    blank_word = blank_word + "_"
guesses = []
def check(new_word, blank_word, user):
    new_word = list(new_word)
    blank_word = list(blank_word)
    if user not in guesses:
        guesses.append(user)
        print(guesses)
    else:
        print(f'You already guessed that!')
    if user in new_word:
        return True
    else:
        return False    

def correct(new_word, blank_word, user):
    new_word = list(new_word)
    blank_word = list(blank_word)
    for i in range(len(new_word)):
        if user == new_word[i]:
            blank_word[i] = user
    blank_word = "".join(blank_word)
    return blank_word

def incorrect(counter):
    counter -= 1
    return counter

def play(new_word, blank_word):
    counter = 10
    while counter > 0:
        user = input("guess a letter > ")
        # check(new_word, blank_word)
        if check(new_word, blank_word, user):
            blank_word = correct(new_word, blank_word, user)
            print(blank_word)
            print(new_word)
            print(counter)
        else:
            counter = incorrect(counter)
            print(blank_word)
            print(new_word)
            print(counter)


(play(new_word, blank_word))