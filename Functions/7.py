'''Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.'''
def chec(string):
    u=0
    l=0
    for i in range(len(string)):
        if string[i].isupper():
            u=u+1
        elif string[i].islower():
            l=l+1
    print("The uppercase count is",u)
    print("The lowercase count is",l)
string=input("Enter your string")
chec(string)

