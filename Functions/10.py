'''Write a Python program to print the even numbers from a given list.'''
def update_list(lis):
    l=[]
    for i in range(len(lis)):
        if (lis[i]%2)==0:
            l.append(lis[i])
    print(l)
update_list([1,2,3,4,5,6,7,8,9,10])

