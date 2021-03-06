import string
# Practice 4 Dictionaries

# Problem 1:
# Given the two lists below, combine them into a dictionary.
def combine(a, b):
    fruit_dict = {}
    for fruit in a:
        index = b[a.index(fruit)]
        fruit_dict.update({str(fruit): index})
    return fruit_dict
# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]
# print(combine(fruits, prices))

# Problem 2:
# Using the result fromthe previous problem, iterate through the dictionary and calcuate the average price of an item.
def average(d):
    average = 0
    counter = 0
    for fruit in d:
        average += d[fruit]
        counter += 1
    return average / counter
# fruits = ['apple', 'banana', 'pear', 'berry']
# prices = [1.2, 3.3, 2.1, 5.0]
# print(average(combine(fruits, prices)))

# Problem 3:
# Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.
# Credits to Merrit for help on this one
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
# d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
# print(unify(d))