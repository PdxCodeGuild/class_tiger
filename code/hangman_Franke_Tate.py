'''
Hangman with Franke and Tate
'''
import random

path ='english.txt'
def loads_words(path):
    with open(path, 'r') as f:
        contents = f.read()

    # split the text file into list strings
    # return the items in the list that have len > 5

    contents_list = contents.split('\n')
    words = []
    for item in contents_list:
        if len(item) > 5:
            words.append(item)
    return words

words = loads_words(path)
random_word = random.choice(words)
print(random_word)
def check_win(user_word):
    # will run every while loop
    # sort both user word and random word, see if they are the same
    a = set(user_word)
    b = set(random_word)
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    return a == b

# Show the user a list of blanks and ask for a letter
# If the guess letter is in the random word, need to update the users word to show where the match occurs
random_word_list = list(random_word)
#user_word_list = list(user_word)

def show_user_status(user_word):
    user_word_list = list(user_word)
    number_letters = len(random_word)
    print_list = [' _ ' for x in range(len(random_word_list))]

    for i in range(len(print_list)):
        if random_word_list[i] in user_word:
            print_list[i] = random_word_list[i]

    printed = ''.join(print_list)
    return printed

def guess_letter(random_word):
    # user has ten guess to guess a given letter
    remaining_guesses = 10
    user_guess = ''
    user_guesses = []
    user_word = []

    while remaining_guesses != 0:
        user_guess = input('Guess a letter > ').lower()
        if user_guess in user_word:
            print('You already guessed that')
            print(f'# of guesses remaining: {remaining_guesses}')
            print(f'You have guessed: {user_word}')
        elif user_guess in random_word_list:
            user_word.append(user_guess)
            print(user_word)
            v = check_win(user_word)
            # print(v)
            if v:
                print(f'Good Job! The word was {random_word}')
                return 'You win!'
        else:
            remaining_guesses -= 1

            print('incorrect, try again')
        print(f'# of guesses remaining: {remaining_guesses}')
        print(f'You have guessed: {user_word}')
        user_guesses.append(user_guess)
        print(show_user_status(user_word))
    print('\nYou lose')
    print(f'The word was {random_word}')
    return user_guesses


guess_letter(random_word)
