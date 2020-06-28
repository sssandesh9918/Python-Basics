'''Write a Python program to check a list is empty or not.'''
n=int(input("Enter the number of input you want to enter"))
l=[]
for i in range(n):
    lis=list(input("Enter your input"))
    l.append(lis)
l=len(lis)
if l==0:
    print("The list is empty")
else:
    print("The list is not empty")