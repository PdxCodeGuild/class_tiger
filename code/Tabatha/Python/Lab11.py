# Calculator

operator_input = input(f'What is the operation you\'d like to perform? > ')

while True:

    if operator_input.lower() == 'done':
        print("DONE")
        break

    else:

        operand_1 = float(input(f' What is the first number? > '))

        operand_2 = float(input(f' What is the second number? >'))

        if operator_input == "+" :
            total = operand_1 + operand_2
        elif operator_input == "-" :
            total = operand_1 - operand_2
        elif operator_input == "*" :
            total = operand_1 * operand_2
        elif operator_input == "/" :
            total = operand_1 / operand_2

        print(f'{operand_1} {operator_input} {operand_2} = {total}')
