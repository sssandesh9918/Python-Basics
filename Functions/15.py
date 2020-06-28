'''Write a Python program to filter a list of integers using Lambda.'''
odd= lambda x: x%2 != 0
result= filter(odd, [1,2,3,4,5,6,7,8,9,10])
print(list(result))