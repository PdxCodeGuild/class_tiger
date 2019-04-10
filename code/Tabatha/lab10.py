# Average Numbers

# nums = [5, 0, 8, 3, 4, 1, 6]

# for num in nums:
#     print(num)
#
# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])
nums = []
while True:
    number = input('enter a number or type "done": ')
    if number.lower() == 'done':
        break
    number = int(number)
    nums.append(number)
    # print(nums)

# print each number while adding them together. divide total by the total amount of numbers.
total = 0
for num in nums:
    # print(num)
    total += num
    # print(total)
    # print("-")
average = total / int(len(nums))
print(f'The average of the list is {average}')
