'''Write a Python script to add a key to a dictionary.'''
dic={0: 10, 1: 20}
n=int(input("Enter the number of key you want to add"))
for i in range(n):
    key=int(input("Enter key you want to add"))
    value=int(input("Enter the value to your key"))
    dic.update({key:value})
print(dic)