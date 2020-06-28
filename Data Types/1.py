'''Write a Python program to count the number of characters (character
frequency) in a string. Sample String : google.com'''

string=input("Enter a string")
count={}
for a in string:
    if a in count:
        count[a] +=1
    else:
        count[a]=1
print(count)