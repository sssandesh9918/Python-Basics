'''Write a Python function to multiply all the numbers in a list.'''
def mul(*args):
    z=1
    for i in range(len(args)):
        z=z*args[i]
    return z
z=mul(8, 2, 3, -1, 7)
print(z)
