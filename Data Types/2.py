'''Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.'''
string=input("Enter your string")
b=len(string)
if b>=4:
    print(string[:2]+string[-2:])
if b in range(2,4):
    print(string[:2]+string[-2:])
if b==1:
    print("Empty String")