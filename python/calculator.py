# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

operation = input('Enter operation(+ - / * %)')

if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif operation == '%':
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
else:
    print("Invalid operation")