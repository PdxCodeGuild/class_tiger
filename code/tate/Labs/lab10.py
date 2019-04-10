# Average Numbers

nums = []
user_input = ''
user_int = 0
running_sum = 0

while True:
    user_input = (input('Append number to list or \'done\': '))
    if user_input.lower() == 'done':
        break
    else:
        while True:
            try:
                user_int= int(user_input)
                break
            except ValueError:
                print('please enter a valid integer')
                continue

    nums.append(user_int)
    print(nums)

for num in nums:
    running_sum += num
avg = running_sum / len(nums)

print(f'Your average is {avg}')
