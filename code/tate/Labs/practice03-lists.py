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

# Problem 2 : Write a REPL which asks useres for a list of numbers, which they enter, until they say 'done.' Then print out the list_cards
def ask_user_list():
    user_input = input('Enter a number (or \done\') > ')
    user_list = []
    while user_input != 'done':

        user_list.append(user_input)
        user_input = input('Enter a number (or \done\') > ')

    print(user_list)

# ask_user_list()

# Problem 3 : write a function that takes a list of numbers and returns True if there is a  even number of even numbers

def even_of_evens(user_list):
    even_counter = 0

    for item in user_list:
        if item % 2 == 0 :
            even_counter += 1

    if even_counter % 2 == 0:
        return True
    else:
        return False

# print(even_of_evens([2,3,4,5,2]))

# Problem 4 : Print out every other element of a list, first using a while loop then a for value in variable:

def every_other(my_list):
    for num in my_list:
        if num % 2 == 0:
            print(num)
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            print(my_list[i])
        i += 1

# every_other([1,2,3,4,5,6,7])

# Problem 5 : write a function that returns the reverse of a list_cards

def reverse_list(user_list):
    list_reversed = []
    for item in user_list:
        list_reversed.insert(0,item)
    return list_reversed
# print(reverse_list([1,2,3,4]))

# Problem 6 : Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(user_list):
    list_less_than_ten = []

    for num in user_list:
        if num < 10:
            list_less_than_ten.append(num)
    return list_less_than_ten

# print(extract_less_than_ten([1,22,2,3,44,55,3]))

# Problem 7 : Write a function to find all common elements between two Lists

def common_elements(list1,list2):
    common_nums=[]
    for n in list1:
        if n in list2:
            common_nums.append(n)
    return common_nums

# print(common_elements([1,2,3,5,6,7],[0,2,33,44,4,5,6]))

# Problem 8 : combine two lists of equal length into one, alternating elements

def combine_lists(list1,list2):
    combined_list=[]
    if len(list1) == len(list2):
        for n in range(len(list1)):
            combined_list.append(list1[n])
            combined_list.append(list2[n])
        return combined_list
    else:
        print('These lists are not worthy')

# Problem 9 : Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number

def find_pair(user_list,target_num):
    for n in user_list:
        # print(n)
        i = 0
        while i < len(user_list):
            if n + user_list[i] == target_num:
                func_output = [n,user_list[i]]
                return func_output

            i += 1
    return 'No pairs met target'

# print(find_pair([5,3,4],7))

# Problem 10 : merge two lists into single list where each element is a list containing two elements from the input list2

def merge_lists(list1,list2):
    lists_merged = []
    item_pair = []
    if len(list1) == len(list2):
        for n in range(len(list1)):
            item_pair = [list1[n],list2[n]]
            lists_merged.append(item_pair)
        return lists_merged
    else:
        print('These lists are not worthy')

# print(merge_lists([1,2,3,4],['a','b','c','d']))

# Problem 11 : Write a function combine all that takes a list of lists and returns a list containing each element from each of the lists_merged
#
def combine_all(user_list):
    combined_list=[]

    for n in user_list:
        for i in range(len(n)):
            combined_list.append(n[i])

    return combined_list

# print(combine_all([[1,2,3],[4,5,6],[7,8,9]]))
