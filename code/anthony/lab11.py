operator_choices = ['+', '-', '*', '/', 'done']
operator = ''
num1 = 0
num2 = 0
solution = 0

while True:
    operator = input('What is the operation you would like to perform? : ')
    while operator not in operator_choices:
        operator = input(f'Enter on of the following: {operator_choices[0]}, {operator_choices[1]}, {operator_choices[2]}, {operator_choices[3]}, {operator_choices[4]} : ')
    if operator == 'done':
        break
    num1 = int(input("What is the first number? : "))
    num2 = int(input("What is the second number? : "))

    if operator == '+':
        solution = num1 + num2
    elif operator == '-':
        solution = num1 - num2
    elif operator == '*':
        solution = num1 * num2
    else:
        soltuion = num1 / num2

    print(f"{num1} {operator} {num2} = {solution}")

print("Goodbye!")