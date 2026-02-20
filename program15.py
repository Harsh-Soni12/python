#name:harshvaya
#enrolment.no:92400527205


'''Write a program to print factorial number using function '''

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

num = int(input("Enter a number: "))

result = factorial(num)

print(f"Factorial of {num} is {result}")


