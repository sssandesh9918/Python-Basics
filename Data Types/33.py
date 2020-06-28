'''Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys
Sample Dictionary'''
dic={}
for i in range(1,16):
    key=i
    value=i*i
    dic.update({key:value})
print(dic)