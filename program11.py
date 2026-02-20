
#name:harshvaya
#enrolment.no:92400527205

'''Write a program to input a number and display Factorial of that 
number. For example, Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120. '''


n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"Factorial of {n} is {fact}")
