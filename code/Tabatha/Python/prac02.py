#Practice Labs 2

#------ Problem 1

def double_letters(x):
    double_x = ""
    for char in x:
        double_x += char + char
    return double_x

# x = (input('Say anything > '))

# print(double_letters(x))
# double_letters('')

#------ Problem 2

def missing_char(phrase):
    missing_char_list = []
    phrase_list = list(phrase)
    for i in range(len(phrase_list)):
        word = phrase_list.copy()
        word.pop(i)
        word = "".join(word)
        missing_char_list.append(word)
    return missing_char_list

# phrase = input('say something > ')
# print(missing_char(phrase))

#------ Problem 3

def last_letter(input_word):
    input_list = list(input_word)
    # print(input_list)
    input_list = sorted(input_list)
    # print(input_list)
    input_list = list(reversed(input_list))
    # print(input_list)
    return input_list[0]
# input_word = input('say something else > ')
# print(last_letter(input_word))

#------ Problem 4

def count_hi(input_hi):
    sub_hi = "hi"
    num_hi = input_hi.count(sub_hi)
    return num_hi
# input_hi = input('say hi > ')
# print(count_hi(input_hi))

#------ Problem 5

def count_input(input_var):
    sub_cat = "cat"
    num_cat = input_var.count(sub_cat)
    sub_dog = "dog"
    num_dog = input_var.count(sub_dog)
    if num_cat == num_dog:
        return True
    else:
        return False
# input_var = input('cats and dogs > ')
# print(count_input(input_var))

#------ Problem 6

def count_char(letter, word):
    letter_counter = word.count(letter)
    return letter_counter
# word = input('input a word > ')
# letter = input('what letter are you looking for? > ')
# print(f'There are {count_char(letter, word)} {letter}\'s in {word}.')

#------ Problem 7

def make_small(the_words):
    now_short = the_words.strip()
    now_small = now_short.lower()
    return now_small

# the_words = input('say stuff > ')
# print(make_small(the_words))

