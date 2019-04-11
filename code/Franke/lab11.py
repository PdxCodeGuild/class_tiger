##### Step 1############
# Ask the user for an operator and each operand. Don't forget that input
# returns a string, which you can convert to a float using float(user_input)
# where user_input is the string you got from input. Below is some sample input/output.


while True:
    Operator = input("what is the operation you'd like to perform? ")
    if Operator == 'done':
        break
    opand1 = int(input(f'what is the first number '))
    opand2 = int(input(f'what is the second number '))

    if Operator == '+':
        sum = opand1 + opand2
        print(f'{opand1} + {opand2} = {sum}')
    elif Operator == '-':
        difference = opand1 - opand2
        print(f'{opand1} - {opand2} = {difference}')
    elif Operator == '*':
        product = opand1 * opand2
        print(f'{opand1} * {opand2} = {product}')
    elif Operator == '/':
        product2 = opand1 / opand2
        print(f'{opand1} / {opand2} = {product2}')
print(f'goodbye!')