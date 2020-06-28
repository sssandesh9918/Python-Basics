'''Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.'''
string=list(input("Enter a string"))
l=len(string)
y=['i','n','g']
if l>=3:
    if string[-3:]==y:
        string.append('ly')
    else:
        string.append('ing')
if l<3:
    pass
c=''
print(c.join(string))
