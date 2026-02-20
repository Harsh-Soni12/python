#name:harshvaya
#enrolment.no:92400527205

'''Write a program to input a number and display whether number is 
prime or not.  '''

n = int(input("Enter a number: "))
flag = 0

for i in range(2, n):
    if n % i == 0:
        flag = 1
        break

if flag == 1:
    print("Not prime")
else:
    print("Prime")

