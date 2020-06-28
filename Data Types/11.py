'''Write a Python program to count the occurrences of each word in a given
sentence.'''
sentence=input("Enter your sentence")
sen=sentence.split( )
occ={}
for a in sen:
    if a in occ:
        occ[a]+=1
    else:
        occ[a]=1
print(sen)
print(occ)