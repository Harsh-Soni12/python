#name:harshvaya
#enrolment.no:92400527205

'''Write a program which accepts a sequence of comma-separated 
numbers from console and generate a list and a tuple which 
contains every number.'''


numbers = input("Enter comma-separated numbers: ")
num_list = numbers.split(",")
num_tuple = tuple(num_list)
print("List:", num_list)
print("Tuple:", num_tuple)

