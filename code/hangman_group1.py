import random
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
        guesses.append(user)
        print(f"Letters already guessed: \n {guesses}")
    else:
        print(f'You already guessed that!')
    if user in new_word:
        return True
    else:
        return False

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



def play():
    play_again = True
    while play_again:
        new_word = word_gen()
        blank_word = blank_gen(new_word)
        guesses = []
        counter = 10
        while counter >= 0:
            if new_word == blank_word:
                print("You won!")
                break
            elif counter ==0:
                print(f"You lose! The word was {new_word}")
                break
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

        play_again = input("Would you like to play again? ")
        if play_again == "no":
            play_again = False


play()
