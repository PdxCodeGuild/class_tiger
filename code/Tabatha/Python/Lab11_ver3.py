
expression = input('I am a Calculator. \nEnter a simple expression or type "done" > ' )

while True:

    if expression.lower() == 'done':
        print("DONE")
        break

    else:
        total = eval(expression)
        print(f'The answer is {total}')