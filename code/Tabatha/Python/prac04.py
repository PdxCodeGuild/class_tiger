

fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

def combine(a, b):
    current_price = dict(zip(a, b))
    return current_price

# print(comb(ine(fruits, prices))

current_price = dict(zip(fruits, prices))

    
def average(a):
    average_price = sum(a.values()) / len(list(a.values()))
    return average_price

# print(average(current_price))

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
output = {}
def first_letter(input):
    for letter in "abcdefghijklmnopqrstuvwxyz" :
        # letter_list = []
        # for key, value in input.items():
        #     if key[0] == letter:
        #         letter_list.append(value)
        letter_list = [value for key, value in input.items() if key[0] == letter]
        # don't need .append because that's what list comps. do. 
        if letter_list:
            output[letter] = sum(letter_list) / len(letter_list)
    return output
print(first_letter(d))




# average values

# create new dictionary for start letter and average






