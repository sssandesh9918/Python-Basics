'''Write a Python program to find if a given string starts with a given character
using Lambda.'''
find= lambda x: 'It starts with the given string' if x.startswith('a') else 'It doesnot starts with the given string'
r=input("Enter a string")
re=find(r)
print(re)



