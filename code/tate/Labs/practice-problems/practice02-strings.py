'''
Practice : Strings

    For each practice problem write a function that returns a value (not just prints it)

'''
# user_string = input('Input the string > ')

# Problem 1 : Get a string from the user, print out another string, doubling every letter

def double_letters(user_string):
    output_string = ''
    for l in user_string:
        output_string += l * 2

    return output_string
# print(double_letters(user_string))

# Problem 2 : write a function that takes a string and returns a list of strigns each missing a different character

def missing_char(user_string):
    string_list = []
    list_string = list(user_string)
    length_list = len(list_string)
    i = 1
    while i < length_list + 1:
        string_list.append(user_string[0:i-1] + user_string[i:length_list])
        i += 1
    return string_list

# print(missing_char(user_string))

# Problem 3 :

def latest_letter(user_string):
    user_list = list(user_string.lower())
    user_list.sort()
    return user_list[-1]

# print(latest_letter('Whatever'))

# Problem 4 :  write a function that returns the number of occurances of 'hi' in a given string_list
def count_hi(user_string):
    list_string = list(user_string)
    length_string = len(list_string)
    length_list = len(list_string)
    count_occurances = 0
    i = 0
    while i < length_list - 1 :
        letter = list_string[i]
        next_letter = list_string[i+1]
        pair_letters = letter + next_letter
        if pair_letters == 'hi':
            count_occurances += 1

        i += 1

    return count_occurances

# count_occurances = count_hi('hi hi hi hi hi')
# print(count_occurances)

# Problem 5 : Write a function that returns True if a string contains the same number of 'cat ' as it does 'dog'

def cat_dog(user_string):
    user_string = user_string.lower()
    cat_count = user_string.count('cat')
    dog_count = user_string.count('dog')

    if cat_count == dog_count:
        return True
    else:
        return False

# print(cat_dog('catdog dog dog'))

# Problem 6 : Return the number of letter occurances in a string

def count_letter(letter,word):
    list_word = list(word)
    list_word.sort()
    word = ''.join(list_word)
    letter_count = word.count(letter)
    return letter_count

# print(count_letter('h','adflsjadhhhskfadsfasd'))


# Problem 7 : Convert input strings to lowercase without any surrounding whitespace

def lower_case(input_str):
    my_string = input_str.strip(' ')
    return my_string.lower()

# print(lower_case('    Superd NNANNAN Batman     '))
















    ########
