'''Write a Python program to remove duplicates from a list.'''
n=int(input("Enter the number of input you want to enter"))
l=[]
for i in range(n):
    lis=list(input("Enter your input"))
    l.append(lis)
for a in l:
    if l.count(a)>1:
        l.remove(a)
print(l)
