# Practice lab 3

#------Problem 1
#---- Ask about the randint, not very random

fruits = ['apples', 'bananas', 'pears', 'grape', 'tomato']
def random_element(fruits):
    import random
    index_len = len(fruits)
    ran_index = random.randint(0, index_len)
    return fruits[ran_index]
# print(random_element(fruits))

#------Problem 2

num_list = []
def make_list(in_num):

    while in_num != "done":
        new_num = int(in_num)
        num_list.append(new_num)
        in_num = (input("Enter a number or type 'done' > "))
        return make_list(in_num)
    return num_list

# in_num = (input("Enter a number or type 'done' > "))
# print(make_list(in_num))

#------Problem 3

num_list1 = [2, 4, 5, 7]
num_list2 = [2, 3, 5, 7]
even_list = []

def check_even(num_list1):
    index_add = 0
    for i in range(len(num_list1)):
        x = num_list1[index_add]
        if x % 2 == 0:
            even_list.append(x)
            index_add += 1
    even_len = len(even_list)
    z = even_len % 2
    if z == 0:
        return True
    else:
        return False
# print(check_even(num_list1))

#---- Problem 4

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# def print_every_other(nums):
    # for i in range(0, len(nums), 2):
    #     print(nums[i])
#     index1 = 0
#     len1 = len(nums)
#     while index1 < len1:
#         print(nums[index1])
#         index1 = index1 + 2
# print(print_every_other(nums))

#------Problem 5

def countdown(nums):
    nums.reverse()
    return nums
# print(countdown(nums))

#------Problem 6

def less_than_ten(nums):
    less_than_ten_list = []
    for i in range(len(nums)):
        if nums[0] < 10:
            x = nums.pop(0)
            less_than_ten_list.append(x)
    return less_than_ten_list
# print(less_than_ten(nums))
# print(nums)

#-------Problem 7

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [3, 4, 5, 6]

# def in_common(list1,list2):
#     for i in range(len(list1[1::])):
#         if i in list2:
#             print(i)
# print(in_common(list1, list2))
        # return

#-------Problem 8


list1 = [1, 2, 3, 8]
list2 = [3, 4, 5, 6]
list3 =[]
def combine(list1, list2):
    while len(list1) > 0 or list2:
        if len(list1) > 0: #if list1: truey, falsey
            list3.append(list1.pop(0))
        if len(list2) > 0:
            list3.append(list2.pop(0))
    return list3

# print(combine(list1, list2))

#------Problem 9 

nums = [5, 6, 2, 1]
target = 7
targets = []
def find_pair(nums):
    x = 0
    for i in range(len(nums)):
        keep_num = nums.copy()
        keep_num2 = nums.copy()
        if nums[x] + nums[i] == target:
            targets.append(keep_num[x])
            targets.append(keep_num2[i])
            x += 1
    return targets
# print(find_pair(nums))

#------ Problem 10

list1 = [1, 2, 3, 8]
list2 = [3, 4, 5, 6]
list3 =[]
def combine2(list1, list2):
    while list1:
        list3.append([list1.pop(0), list2.pop(0)])
    return list3
# print(combine2(list1, list2))

#------ Problem 11

nums2 = [[5,2,3],[4,5,1],[7,6,3]]
nums3 = []
def combine3(nums2):
    nums3 = [x for y in nums2 for x in y]
    # for x in nums2:
    #     for y in x:
    #         nums3.append(y)
    return nums3


len_fib = 40
fib = []
a = 0
b = 1
def fibonacci(len_fib, a = 0, b = 1,):
    if b < len_fib:
        fib.append(b)
        a, b = b, a + b
    else:
        return fib
    return fibonacci(len_fib, a, b)
# print(fibonacci(len_fib))
 
nums_list = [1, 2, 3, 5, 7, 6, 0]
def minimum(nums):
    nums_list.sort()
    return nums_list[0]

def maximum(nums):
    nums_list.sort()
    return nums_list[-1]

def mean(nums):
    mean_num = sum(nums_list) / len(nums_list)
    return mean_num
    

# print (mean(nums))

nums_list2 = [1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5]
def remove_dup(nums_list2):
    unique_nums = []
    for i in nums_list2:
        if i not in unique_nums:
            unique_nums.append(i)
    # unique_nums = [i for i in nums_list2 if i not in unique_nums]
    return unique_nums

print(remove_dup(nums_list2))





    




