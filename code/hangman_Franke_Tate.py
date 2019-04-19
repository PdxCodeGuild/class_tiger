'''
Hangman with Franke and Tate
'''
import random

path ='english.txt'
def loads_words(path):
    with open(path,'r') as f:
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
# random_word = random.choice(words)
random_word = 'hello'
random_word_list = list(random_word)

def guess_letter(random_word):
    # user has ten guess to guess a given letter
    count_guesses = 0
    user_guess = ''
    user_guesses = []
    user_word = []

    # if the the letter guessed is in the random_word list of letters,
    # run the update status and show the users updated word with the new matching letter
    # need to be checking if user word == random word, and if it does, break out of the while loop and return you win

    while count_guesses <= 10:
        user_guess = input('Guess a letter > ').lower()
        count_guesses += 1
        if user_guess in random_word_list:
            user_word.append(user_guess)
            print(user_word)
            if check_win(user_word) == True:
                return 'whatever'

        else:
            print('incorrect, try again')
        user_guesses.append(user_guess)

    return user_guesses


def check_win(user_word):
    # will run every while loop
    user_word_list = list(user_word)

    # sort both user word and random word, see if they are the same
    user_word_list.sort()
    random_word_list.sort()

    if user_word_list == random_word_list:
        print('Winner')
        return True
    else:
        print('Keep guessing')
        return False

guess_letter(random_word)


# Show the user a list of blanks and ask for a letter
# If the guess letter is in the random word, need to update the users word to show where the match occurs

# def show_user_status(updated_word):
#     number_letters = len(random_word)
#
#     print((' _ ') * number_letters )
#
# #If they guess a letter that is in the words variable, show the list of blanks with that letter filled in
#
# #
# show_user_status(user_word)




# print(guess_letter('g'))
