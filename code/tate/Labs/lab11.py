# Simple Calculator

calc_result = 0

while True:
    print('Type \'done\' to quit.')
    user_operator = input('What is the operation you would like to perform? \n (+, -, *, /, or arithmetic) : ')

    if user_operator.lower() == 'done':
        print('Goodbye!')
        break

    while user_operator not in ['+','-','*','/','done','arithmetic']:
        print('Invalid operator input')
        user_operator = input('What is the operation you would like to perform? \n (+, -, *, /, arithmetic or \'done\') : ')

    # Would change this to not need the following if statement when we cover functions
    if user_operator.lower() == 'done':
        print('Goodbye!')
        break

    if user_operator == 'arithmetic':
        calc_result = eval(input('what would you like to evaluate? : '))
        print(f'Your result is {calc_result}')
        continue

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

    print(f'Your result is {calc_result}')
