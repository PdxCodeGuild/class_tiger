########Step 1#########################

nums = [5, 0, 8, 3, 4, 1, 6]
sum = 0
average1 = []
for i in nums:
    sum += i
print(sum/len(nums))


########Step2  not empty list but 0 since you can't add int + list
# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done',
# then calculate and display the average. The following code demonstrates how to add an element to the end of a list.#
nums2 = [5, 0, 8, 3, 4, 1, 6]
sum2 = 0
average = 0
while True:
    num = input('enter number or type done: ')
    if num == 'done':
        break
    else:
        sum2 += int(num)
        average = sum2/len(nums2)
    print(f'average: {average}')


