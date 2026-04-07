# name: harshvaya
# enrolment.no: 92400527205

'''Write a program to read text file having number and display all 
numbers with total and average at the last. (Manually prepare a file 
having some numbers and then read it)'''

with open("number.txt","r") as file:
    total = 0      
    count = 0
    print("Numbers in file:")

    for line in file:
        num = int(line.strip())
        print(num)
        
        total += num
        count += 1


average = total / count  

print("Total:", total)
print("Average:", average)
