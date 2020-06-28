'''Write a Python program to find the length of a tuple'''
#Using given
tupl=('1','2','3','4','5','6','Hello','World!')   
print("The length of the tuple is",len(tupl))
#Taking input
n=int(input("Enter the number of items you want to enter"))
t=[]
for i in range(n):
    li=list(input("Enter your element"))
    t.append(li)
tup=tuple(t)
print("The length of the tuple is",len(tup))

