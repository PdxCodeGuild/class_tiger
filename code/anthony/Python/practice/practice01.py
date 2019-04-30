# Practice 1 Fundamentals

# Problem 1:
# Write a function that tells whether a number is even or odd
def is_even(x):
    if x % 2 == 0:
        return True
    return False
    
# Problem 2:
# Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative
def opposite(a, b):
    if a < 0 and b > 0:
        return True
    elif a > 0 and b < 0:
        return True
    return False

# Problem 3:
# Write a function that returns True if number within 100
def near_100(num):
    if abs(100 - num) <= 10:
        return True
    return False

# Problem 5:
# Print out the powers of 2 from 2^0 to 2^20
def pow_two():
    num = 2
    exponant = 0
    while num < pow(2, 20):
        num = pow(2, exponant)
        print(num)
        exponant += 1
