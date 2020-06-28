'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.'''
n=int(input("Enter the number of strings you want to enter"))
str=[]
for j in range(n):
    string=list(input("Enter your string"))
    str.append(string)
count=0
for i in range(len(str)):
    l=len(str[i])
    if l>=2 and (str[i])[0]==(str[i])[-1]:
        count=count+1
print(count)