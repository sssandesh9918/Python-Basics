'''Write a Python function that takes a list and returns a new list with unique
elements of the first list.'''
def uniq(b):
    for a in b:
        if b.count(a)>1:
            b.remove(a)
    print(b)
b=[]
n=int(input("Enter the number of elements you want to enter"))
for i in range(n):
    elem=list(input("Enter elements"))
    b.append(elem)
uniq(b)
