#name:harshvaya
#enrolment.no:92400527205


'''Write a program to read names from keyboard and store into text 
file '''

file = open("names.txt", "w")
n = int(input("how many name do you want to enter ? : "))
for i in range(n):
    name = input("enter name : ")
    file.write(name + "\n")

file.close()
print("names saved successfully!") 
