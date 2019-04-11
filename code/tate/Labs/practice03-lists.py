'''
    Practice Problems : Lists

'''

# Problem 1 : Write a function that uses random.randint to generate an index, use that index to pick a random element of a list and return it

import random

def random_element(mylist):
    length_list = len(mylist)
    random_list_element = mylist[random.randint(0,length_list - 1)]
    return random_list_element

#
# print(random_element(['apple','cherry','pear']))
