'''Write a Python program to sort a list of dictionaries using Lambda.'''
sort=lambda x: x[1]
dic=[{2: 20, 4: 40, 5: 50, 1: 10, 2: 20, 3: 30,  6: 60}]
def func(l):
    return l[1]
dic.sort(key=sort)
print(dic)