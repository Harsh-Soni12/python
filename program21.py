#name:harshvaya
#enrolment.no:92400527205



'''Write a program to read any text file line by line '''

file name = input("Enter the file name: ")

with open(file name, "r") as file:
    for line in file:
        print(line,end="")
