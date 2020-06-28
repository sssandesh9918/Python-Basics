'''Write a Python program to change a given string to a new string where the first
and last chars have been exchanged.'''
given_str=list(input("Enter a string"))
temp=[]
temp=given_str[0]
given_str[0]=given_str[-1]
given_str[-1]=temp
print(''.join(given_str))