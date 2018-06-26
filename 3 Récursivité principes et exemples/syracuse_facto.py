import random


def facto(n):
    if n==1:
        return 1
    return n*facto(n-1)

def syracuse_iter(n):
    while n!=1 and n!=0:
        print (n)
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
            

def syracuse_rec(n):
    print(n)
    if n==0 or n==1:
        return 1
    elif n%2==0:
        return syracuse_rec(n/2)
    else:
        return syracuse_rec(3*n+1)
        