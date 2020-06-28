'''Write a Python script to check whether a given key already exists in a
dictionary.'''
dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
n=int(input("Enter the number of key you want to add"))
for i in range(n):
    key=int(input("Enter key you want to add"))
    if key in dic:
        print("The key already exists")
    else:
        print("The key doesnot exists")