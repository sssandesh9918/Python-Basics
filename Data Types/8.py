'''Write a Python program to remove the nth index character from a nonempty string.'''
string=list(input('Enter a string'))
a=len(string)
if a>=1:
    string.pop(-1)
print(''.join(string))
