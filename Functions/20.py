'''Write a Python program to find intersection of two given arrays using
Lambda.'''
lis=[1,2,3,4,5]
lis1=[3,4,5,6,7]
che=filter(lambda x: x in lis,lis1)
print(list(che))

