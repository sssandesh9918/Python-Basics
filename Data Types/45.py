'''Write a Python program to find the index of an item of a tuple.'''
tup=('1','2','3','4','5','6','Hello','World!')
print(tup)
element=input("Enter item to find the index")
for i in range(len(tup)):
    if tup[i]==element:
        print("The index is %d"%(i))
