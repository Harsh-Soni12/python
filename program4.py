#name:harshvaya
#enrolment.no:92400527205


'''Write a program to input Principal Amount, Rate and Year and 
display Compound Interest'''

# Program 4
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = int(input("Enter Time in Years: "))

CI = P * ((1 + R/100) ** T) - P
print("Compound Interest:", CI)

