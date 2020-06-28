'''Write a Python program to check whether all dictionaries in a list are empty or
not.'''
li=[{},{},{}]
lis=[{1,2},{},{}]
liss=[{1,2,3},{},{}]
lisss=[{},{},{},{}]
print(all(not d for d in li))
print(all(not d for d in lis))
print(all(not d for d in liss))
print(all(not d for d in lisss))