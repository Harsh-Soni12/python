#name:harshvaya
#enrolment.no:92400527205

'''Write a Python Program to input marks of 4 subjects and display 
Total, Percentage, Result and Grade. If student is fail (<40) in any 
subject then Result should be displayed as “FAIL” and Grade should 
be displayed as “With Held '''

# Program 8

print("Enter marks for 4 subjects (out of 100):")

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))

total_marks = sub1 + sub2 + sub3 + sub4
percentage = total_marks / 4

# Check subject-wise fail first
if sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33:
    grade = "Fail"
else:
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"

print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)

