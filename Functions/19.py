'''Write a Python program to create Fibonacci series upto n using Lambda.'''
#0.1.1.2.3.5.8.13.21...
def fib(n):
    lis=[0,1]
    fib=any(map(lambda _: lis.append(sum(lis[-2:])), range(2,n)))
    return lis[:n]
n=int(input("Enter the value of n upto which you want to generate the Fibonacci series"))
print(fib(7))

