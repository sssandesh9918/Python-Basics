'''Write a Python program to reverse a string.'''
l=[]
def reverse(string):
    for i in range((len(string)-1),-1,-1):
        l.append(string[i])
    return l
string=input("Enter your string")
reverse(string)
print(''.join(l))