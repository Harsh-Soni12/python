#name:harshvaya
#enrolment.no:92400527205

'''Write a program to print all numbers which are divisible by 7 
between 1 to 200.  '''

# Program 10
print("Numbers divisible by 7 between 1 and 200:")
for i in range(1, 201):
    if i % 7 == 0:
        print(i, end=" ")

