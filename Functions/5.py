'''Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.'''
#using inbuilt function
import math
print(math.factorial(4))
#using user defined function
def fact(n):
    z=1
    if n==0:
        return 1
    for i in range(n,0,-1):
        z=z*i
    return z
n=int(input("Enter a non-negative number to find the factorial of"))
try:
    if n>0:
        z=fact(n)
    print(z)
except:
    print("Please enter positive number only")

