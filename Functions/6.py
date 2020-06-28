'''Write a Python function to check whether a number is in a given range.'''
def che(a,b,num):
    r=range(a,b+1)
    if num in r:
        print("The number is in the given range")
    else:
        print("The number is not in given range")
a=int(input("Enter the starting range"))
b=int(input("Enter the ending range"))
num=int(input("Enter the number you want to check"))
che(a,b,num)