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

# Problem 3 : write a function that returns the number of occurances of 'hi' in a given string_list

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

#
# count_occurances = count_hi('hi hi hi hi hi')
# print(count_occurances)


















    ########
