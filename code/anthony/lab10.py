import string

nums = []
num_sum = 0
num_average = 0

while True:
    user_input = input("Enter a number or type 'done' : ")
    while True:
        try:
            user_input = int(user_input)
            break
        except ValueError:
            if user_input == 'done':
                break
            else:
                user_input = input("Enter a number or type 'done' : ")
    # while user_input != string.digits and user_input != 'done':
    #     user_input = input("Enter a number or type 'done'")
    
    if user_input == 'done':
        break
    else:
        nums.append(user_input)

if len(nums) > 0:
    for i in range(len(nums)):
        num_sum += nums[i]
    num_average = num_sum / len(nums)
    print(f"Average: {num_average}")
else:
    print("You did not enter a number.")
