
#name:harshvaya
#enrolment.no:92400527205


'''Write a program to input 2 number and an arithmetic operator. 
Display the result accordingly.'''



#program2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    print("Result:", a / b)
else:
    print("Invalid Operator")

