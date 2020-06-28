'''Write a Python function that takes a list of words and returns the length of the
longest one.'''
def func(a):
    b=[]
    for i in range(a):
        words=list(input("Enter words"))
        b.append(words)
    print(b)
    c=[]
    for j in range(len(b)):
        c.append(len(b[j]))
    print(max(c))
a=int(input("Enter the number of words you want to enter"))
func(a)