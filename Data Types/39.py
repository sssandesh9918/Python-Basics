'''Write a Python program to unpack a tuple in several variables.'''
tup=('1','2','3','4','5')
tu=(1,3,4,5,6)
for i in range(len(tup)):
    a,b,c,d,e=tup
print(a+b+c+d+e)
for i in range(len(tu)):
    a,b,c,d,e=tu
print(a+b+c+d+e)