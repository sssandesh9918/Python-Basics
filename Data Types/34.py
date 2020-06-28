#Write a Python script to merge two Python dictionaries.
dic={}
n=int(input("Enter the number of key you want to add"))
for i in range(n):
    key=int(input("Enter key you want to add"))
    value=int(input("Enter the value to your key"))
    dic.update({key:value})
dic1={}
n=int(input("Enter the number of key you want to add"))
for i in range(n):
    key=int(input("Enter key you want to add"))
    value=int(input("Enter the value to your key"))
    dic1.update({key:value})
dic.update(dic1)
print(dic)