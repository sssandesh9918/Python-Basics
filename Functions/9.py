'''Write a Python function that takes a number as a parameter and check the
number is prime or not.'''
def check_prime(n):
    if n==1:
        print("It is not prime number")
    elif n==2:
        print("It is prime number")
    else:
        for i in range(2,n):
            if n%i==0:
                print("It is not prime number")
                break
            else:
                print("It is prime number")
                break
n=int(input("Enter the number you want to check"))
check_prime(n)