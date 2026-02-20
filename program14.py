
#name:harshvaya
#enrolment.no:92400527205


'''Write a program to print all prime numbers between 1 to 100. '''

for n in range(1, 101):

    if n > 1:
        flag = 0

        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break

        if flag == 0:
            print(n, end=" ")
            # print(n)

            
