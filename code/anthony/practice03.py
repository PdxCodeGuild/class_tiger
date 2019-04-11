import random
# Practice problems

# Problem 1:
# Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.
def random_element(a):
    rand = random.randint(0, len(a))
    return a[rand - 1]
# fruits = ['apples', 'bananas', 'pears']
# print(random_element(fruits))

# Problem 2:
# Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.
def add_list():
    user_input = 0
    user_list = []
    user_input = input("Enter a number (or 'done'): ")
    while user_input != 'done':
        user_list.append(user_input)
        user_input = input("Enter a number (or 'done'): ")
        
    return user_list
# print(add_list())

# Problem 3:
# Write a function that takes  a list of numbers, and returns True if there is an even number of even numbers.
def eveneven(a):
    counter = 0
    for x in a:
        if x % 2 == 0:
            counter += 1
    if counter % 2 == 0:
        return True
    return False
# print(eveneven([5, 5, 2]))

# Problem 4:
# Print out every other element of a list, first using a while loop, then using a for loop
def while_every_other(nums):
    n = 0
    every_other = []
    while n < len(nums):
        every_other.append(n)
        n += 2
    return every_other
def for_every_other(nums):
    every_other = []
    for n in range(0, len(nums), 2):
        every_other.append(n)
    return every_other
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(while_every_other(nums))
# print(for_every_other(nums))

# Problem 5:
# Write a function that returns the reverse of a list
def reverse_list(nums):
    nums.reverse()
    return nums
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#print(reverse_list(nums))

# Problem 6:
# Write function to move all the elemts of a list with value less than 10 to a new list and return it
def extract_less_than_ten(nums):
    new_list = []
    for num in nums:
        if num < 10:
            new_list.append(num)
    return new_list
# nums = [0, 1, 2, 3, 4, 12, 83, 5, 6, 7, 8]
# print(extract_less_than_ten(nums))

# Problem 7:
# Write a function to find all common elements between two list
def common_elements(nums1, nums2):
    counter = 0
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                counter += 1
    return counter
# nums1 = [3, 5, 7, 9, 11, 12]
# nums2 = [4, 5, 6, 7, 8, 9]
# print(common_elements(nums1, nums2))

# Problem 8:
# Write a function to combine two lists of equal length into one, alternating elements
def combine(nums1, nums2):
    combined_list = []
    if len(nums1) != len(nums2):
        return 0
    for n in range(0, len(nums1)):
        combined_list.append(nums1[n])
        combined_list.append(nums2[n])
    return combined_list
# nums1 = [3, 5, 7, 9, 11, 12]
# nums2 = [4, 5, 6, 7, 8, 9]
# print(combine(nums1, nums2))
    
# Problem 9:
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
def find_pair(nums, target):
    for num in nums:
        for n in nums:
            if num + n == target:
                return num, n
# nums = [0, 1, 2, 3, 4, 5]
# target = 7
# print(find_pair(nums, target))

# Problem 10:
# Write a function that merges two lists into a single list, where each element of teh output list is a list 
# containing two elemets, one from each of the input lists.
def merge(nums1, nums2):
    combined_list = []
    if len(nums1) != len(nums2):
        return 0
    for n in range(0, len(nums1)):
        working_list = []
        working_list.append(nums1[n])
        working_list.append(nums2[n])
        combined_list.append(working_list)
    return combined_list
# nums1 = [3, 5, 7, 9, 11, 12]
# nums2 = [4, 5, 6, 7, 8, 9]
# print(merge(nums1, nums2))


# Problem 11:
# Write a functin combine_all that takes a list of lists, and returns a list containing each element from each of the lists
def combine_all(nums1, nums2, nums3):
    new_list = []
    for n in nums1:
        new_list.append(n)
    for n in nums2:
        new_list.append(n)
    for n in nums2:
        new_list.append(n)
    return new_list
# nums1 = [3, 5, 7, 9, 11, 12]
# nums2 = [4, 5, 6, 7, 8, 9]
# nums3 = [1, 2, 3, 4, 5]
# print(combine_all(nums1, nums2, nums3))

# Problem 12:
# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers
def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)
def fibonacci_list(max):
    num = 0
    fib_list = []
    while num < max:
        fib_list.append(fibonacci(num))
        num += 1
    return fib_list
# print(fibonacci_list(8))

# Problem 13:
# Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.
def minimum(nums):
    min = nums(0)
    for num in nums:
        if num < min:
            min = num
    return min
def maximum(nums):
    max = nums(0)
    for num in nums:
        if num > max:
            max = num
    return max
def mean(nums):
    mean = 0
    for num in nums:
        mean += num
    return mean / len(nums)         

# Problem 14:
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.
def find_unique(nums):
    current_index = 0
    for num in nums:
        current_index = nums.index(num) + 1
        if current_index >= len(nums):
            break
        for i in range(current_index, len(nums) -1):
            if num == nums[current_index]:
                nums.pop(current_index)
    return nums
# nums = [1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 7]
# print(find_unique(nums))