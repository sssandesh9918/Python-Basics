'''Write a Python program to sort a list of tuples using Lambda.'''
sort=lambda x: x[0]
lis=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def func(l):
    return l[1]
lis.sort(key=sort)
print(lis)