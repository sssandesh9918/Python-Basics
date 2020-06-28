'''Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.'''
a=list(input("Enter a string"))
b=list(input("Enter another string"))
temp=a[0:2]
a[0:2]=b[0:2]
b[0:2]=temp
c=""
print(c.join(a)+" "+c.join(b))