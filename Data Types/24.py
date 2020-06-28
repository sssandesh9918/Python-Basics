'''Write a Python program to clone or copy a list.'''
n=int(input("Enter the number of input you want to enter"))
l=[]
for i in range(n):
    lis=list(input("Enter your input"))
    l.append(lis)
co=l.copy()
print(co)