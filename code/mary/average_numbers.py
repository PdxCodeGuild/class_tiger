# average_numbers.py
nums_list = []
for num in nums_list:
    print(num)
while True:
    user_number = input("Enter a number, or 'done'.")
    if user_number == 'done':
        break
    else:
        user_number = int(user_number)
        nums_list.append(user_number)
print(f"The sum is {sum(nums_list)}")
x = sum(nums_list) / len(nums_list)
print(f"The average is {x}")
