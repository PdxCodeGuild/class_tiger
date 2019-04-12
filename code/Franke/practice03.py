#Problem 1
# Write a function using random.
# randint to generate an index, use that index
# to pick a random element of a list and return it.
import random
def random_element(a):
    return a[random.randint(0,len(a))]

l=['max','joe','yannix','paula']
random_element(l)

#Problem 2
##Write a REPL which asks users for a list of numbers,
# which they enter, until they say 'done'. Then print out the list.

def enter_numbers(number):
    list=[]
    while True:
        d = input("Enter a number (or 'done'): ")
        if d == 'done':
            break
        else:
            return list.append(int(d))

#Problem 3
#Write a function that takes a list of numbers,
#and returns True if there is an even number of even numbers.
def eveneven(g):
    return (sum(i for i in g if g.index(i) % 2 == 0))%2 == 0

eveneven([5, 6, 2])


#Problem 4
#Print out every other element of a list,
# first using a while loop, then using a for loop.
def print_every_other2(nums):
    a = nums[:-1:2]
    for i in a:
        print(a)

nums = [0, 1, 2, 30, 4, 5, 60, 7, 8]

print_every_other2(nums)

#Problem 5
#Write a function that returns the reverse of a list.

def reversing(nums):
    return list(nums[::-1])

nums = [0, 1, 2, 30, 4, 5, 60, 7, 8]
print(reversing(nums))

#Problem 6
#Write a function to move all the elements of a list
# with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    new_list =[i for i in nums if i < 10]
    return new_list

nums = [0, 1, 2, 30, 4, 5, 60, 7, 8]
print(extract_less_than_ten(nums))


#Problem 7
#Write a function to find all common elements between two lists.

def common_elements(nums1, nums2):
    li_dif = [i for i in nums1 if i in nums1 and i in nums2]
    return li_dif

num1 = [2,4,8,9]
num2 = [2,9,3,9]

print(common_elements(num1, num2))

#Problem 8
#Write a function to combine two lists of
#  equal length into one, alternating elements.

def combine(nums1, nums2):
    big_list = []
    big_list = [None]*(len(nums1)+len(nums2)) #define the len of final list
    big_list[::2] = nums1 # populates every first element with list 1 elmts
    big_list[1::2] = nums2 #populates every first element with list 2 elmts
    return big_list

print(combine(['a','b','c'],[1,2,3]))



#Problem 9
#Given a list of numbers, and a target number, find a pair of numbers
# from the list that sum to a target number
def find_pair(nums, target):
    pair = [(i, target-i) for i in nums if (target - i) in nums and i < (target-i)]
    return pair

nums = [10,20,30,40,50]
target = 70

print(find_pair(nums,target))
#Optional: return a list of all pairs of numbers that sum to a target value.

#Problem 10
#Write a function that merges two lists into a single list,
#  where each element of the output list is a list containing two elements,
# one from each of the input lists.
# Zip two list to iterate over both zip makes them tuples so they stay distinct ele
def merge(a,b):
    c = []
    for i,z in zip(a,b):
        c += [a[a.index(i)],b[b.index(z)]]
    return c

a = [5,2,1]
b = [6,8,2]

print(merge(a,b))

#Problem 11
#Write a function combine_all that takes a list of lists,
#and returns a list containing each element from each of the lists.
#to combine list of list start selecting down
def combine_all(nums):
    c =[]
    for i in nums:
        for j in i:
            c.append(j)
    return c

nums = [[5,2,3],[4,5,1],[7,6,3]]
print(combine_all(nums))

#Problem 12
#Write a function that takes n as a parameter,
# and returns a list containing the first n Fibonacci Numbers.

def fibonacci(n):
    first_fibs = []
    while n in range(n):
        if n == 0 or n == 1:
            return 1
        else:
            first_fibs.append(fibonacci(n-1) + fibonacci(n-2))
    return first_fibs


#Problem 13
#Write functions to find the minimum,
# maximum, mean, and (optionally) mode of a list of numbers.

def minimum(nums):
    '''this returns the minimum value in a list of numbers '''
    return min(nums)

def maximum(nums):
    return max(nums)

import statistics as s

def mean(nums):
    return s.mean(nums)

def mode(nums): # (OPTIONAL)
   return s.mode(nums)

#Problem 14
#Write a function which takes a list as a
## parameter and returns a new list with any duplicates removed.

def find_unique(nums):
    no_dupes =[]
    for i in nums:
        if i not in no_dupes:
           no_dupes.append(i)
    return no_dupes

nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

print(find_unique(nums))