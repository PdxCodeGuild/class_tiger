# simple_calculator.py
op_list = ["+", "-", "*", "/"]

while True:
    select_op = input("What is the operation you would like to perform? Type 'done' if finished.")
    if select_op == "done":
        break
    else:
        num1 = input(f"What is the first number?")
        num2 = input(f"What is the second number?")
        num1 = int(num1)
        num2 = int(num2)
        if select_op == "+":
            print(num1 + num2)
        elif select_op == "-":
            print(num1-num2)
        elif select_op == "*":
            print(num1 * num2)
        elif select_op == "/":
            print(num1/num2)
