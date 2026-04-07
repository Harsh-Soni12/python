#name:harshvaya
#enrolment.no:92400527205

'''Write a Python Program to create a function which accepts 3 
arguments. (2 numbers and one arithmetic operator). Display 
answer accordingly '''


def calc(a, b, o):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
            return a / b
    else:
            return "Error: Division by zero"
    
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
o = input("Enter operator (+, -, *, /): ")

result = calc(a, b, o)
print("Answer:", result)
