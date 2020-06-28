'''Write a Python program to add an item in a tuple.'''
tup=('1','2','3','4','5','6','hello','world')
b=list(tup)
b.append(input("Enter element to append"))
tup=tuple(b)
print(tup)