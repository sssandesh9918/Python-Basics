'''Write a Python program to remove an item from a tuple.'''
tup=('1','2','3','4','5','6','Hello','World!') 
lis=list(tup)
lis.remove('6')
tup=tuple(lis)
print(tup)