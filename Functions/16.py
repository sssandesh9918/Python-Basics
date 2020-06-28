'''Write a Python program to square and cube every number in a given list of
integers using Lambda.'''
func= lambda x: x**2
cube= lambda x: x**3
result= map(func, [1,2,3,4,5,6,7,8,9,10])
r= map(cube, [1,2,3,4,5])
print(list(result))
print(list(r))