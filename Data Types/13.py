'''Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).'''
string=input("Enter comma seperated sequence").split(',')
c=sorted(list(set(string)))
print(','.join(c))