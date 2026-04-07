#name: harshvaya
#enrolment.no: 92400527205

'''Write a program to compute the frequency of the words from the 
input. The output should output after sorting the key 
alphanumerically. 
Suppose the following input is supplied to the program: 
“Hello There this is Python. Python is good” 
Then output shall be as follows : 
Hello : 1 
There : 1 
This : 1 
is : 2 
Python : 2 
Good : 1  '''

text = "hello there this is python. python is good"

# Remove punctuation
text = text.replace(".", "").replace(",", "")

# Split into words
words = text.split()

freq = {}

for word in words:
    word = word.capitalize()   # Make first letter uppercase
    
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Sort and print
for word in sorted(freq):
    print(f"{word} : {freq[word]}")
