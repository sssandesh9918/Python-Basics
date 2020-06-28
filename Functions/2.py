'''Write a Python function to sum all the numbers in a list.'''
def add(*args):
    s=sum(args)
    return s
s=add(1,2,3,4,5)
print(s)
