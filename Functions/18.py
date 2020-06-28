'''18. Write a Python program to check whether a given string is number or not
using Lambda.'''
chec=lambda x: True if r.isnumeric() else False
r=input("Enter a string")
re=chec(r)
print(re)