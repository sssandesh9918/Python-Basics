'''Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).'''
n=int(input("Enter the number of key you want to add"))
dic={}
for i in range(1,n+1):
    key=i
    value=i*i
    dic.update({key:value})
print(dic)