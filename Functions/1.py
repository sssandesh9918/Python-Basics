'''Write a Python function to find the Max of three numbers.'''
def highest(x,y,z):
    return(max(x,y,z))
a=input("Enter first number")
b=input("Enter second number")
c=input("Enter third number")
m=highest(a,b,c)
print("The max of three numbers is ",m)