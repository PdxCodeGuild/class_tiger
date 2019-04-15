'''
Practice 04 : Dictionaries
'''
import string

# Problem 1

def combine (a,b):
    return dict(zip(a,b))

p01_result = combine(['apple','pear','banana'],[1,2,3])

# Problem 2

def average_values(dict_input):

    average_nums = []

    for n in dict_input:
        average_nums.append(dict_input[n])

    my_average= sum(average_nums)/len(average_nums)
    return my_average

# print(average_values(p01_result))

# Problem 3

def unify(d):
    output = {}
    for char in string.ascii_letters:
        letter_list = []
        for key, value in d.items():
            if key[0]==char:
                letter_list.append(value)
        if letter_list:
            output[char] = sum(letter_list)/len(letter_list)
    return output



print(unify({'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}))
