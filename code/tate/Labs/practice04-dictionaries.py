'''
Practice 04 : Dictionaries
'''

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

print(average_values(p01_result))

# Problem 3


def average_similar_keys(dict_input):

    my_keys = dict_input.keys()

    my_keys.sort()

print(average_similar_keys({'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}))
