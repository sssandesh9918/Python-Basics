'''Write a Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.'''
string=input("Enter a string")
b=string.find('not')
c=string.find('poor')
d=c+4
str=list(string)
if 'not' in string:
    if 'poor' in string:
        str[b:d]='good'
        print(''.join(str))
    else:
        print(''.join(str))
else:
    print(''.join(str))