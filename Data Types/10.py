'''Write a Python program to remove the characters which have odd index
values of a given string.'''
string=list(input("Enter a string"))
j=[]
for i in range(len(string)):
    if (i%2)==0:
        j.append(string[i])
print(''.join(j))