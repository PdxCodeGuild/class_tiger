#Problem 1
#Given a the two lists below, combine them into a dictionary.

def combine(a, b):
    return {key: value for key,value in zip(a,b)}

fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

print(combine(fruits,prices))
#Problem 2
#Using the result from the previous problem, iterate
# through the dictionary and calculate the average price of an item.
#To get values only
def average(d):
    return round(sum(d.values())/len(d),2)

combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
print(average(combined) )

#Problem 3
#Average numbers whose keys start with the same letter.
# Output a dictionary containing those
# letters as keys and the averages.
import string as s
def unify(d):
    output = {}
    for letter in s.ascii_lowercase: #get all letter pick 1 each time
        values = []
        for key,value in d.items(): #make dict malleable and choose
            if key[0] == letter: ##you have to compare it to 1 alphaletter at the time
                values.append(value)
        if values:                  ### if there's something in values
            output[letter] = round(sum(values)/len(values),2) #populate output one at the time
    return output

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}

print(unify(d))





print(unify(d))

