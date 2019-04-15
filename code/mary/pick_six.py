#pick_6.py
import random
win_nums = []
user_nums = []
def pick6(win_nums, user_nums):
    for i in range(0,6):
        x = random.randint(1, 99)
        y= random.randint(1, 99)
        win_nums.append(x)
        user_nums.append(y)
    return(win_nums,user_nums)
winning = pick6(win_nums, user_nums)
print(winning)
