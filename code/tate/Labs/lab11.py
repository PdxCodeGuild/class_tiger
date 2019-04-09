# Simple Calculator

calc_result = 0

while True:
    print('Type \'done\' to quit.')
    user_operator = input('What is the operation you would like to perform? \n (+, -, *, or /) : ')

    if user_operator.lower() == 'done':
        print('Goodbye!')
        break

    while user_operator not in ['+','-','*','/','done']:
        print('Invalid operator input')
        user_operator = input('What is the operation you would like to perform? \n (+, -, *, /, or \'done\') : ')

    # Would change this to not need the following if statement when we cover functions
    if user_operator.lower() == 'done':
        print('Goodbye!')
        break

    operand1 = int(input('What is the first number? : '))
    operand2 = int(input('What is the second number? : '))

    if user_operator == '+':
        calc_result = operand1 + operand2
    elif user_operator == '-':
        calc_result = operand1 - operand2
    elif user_operator == '*':
        calc_result = operand1 * operand2
    elif user_operator == '/':
        calc_result = operand1 / operand2

    print(calc_result)
