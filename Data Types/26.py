'''Write a Python program to insert a given string at the beginning of all items in
a list.'''
li=[1,2,3,4,5]
string='emp'
for i in range(len(li)):
    li[i]=string+str(li[i])
print(li)