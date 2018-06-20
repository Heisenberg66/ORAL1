def fibo_recursif(n):
    if n ==0:
        return 0
    if n==1 :
        return 1
    else:
        return fibo_recursif(n-1)+fibo_recursif(n-2)



def fibo_dynamique_iter(n):
    if n == 0:
        return 0
    if n==1:
        return 1
    x,y = 0,1
    for i in range (n-1):
        x,y=y,x+y
    return y
    



def fibo_dynamique_rec(n):
    track = [0]*(n+1)
    return fiboDynRec(n,track)
    
def fiboDynRec(n,track):
    if n ==0 or n==1:
        track[n]=n
        return n
    elif track[n]>0:
        return track[n]
    else:
        track[n]= fiboDynRec(n-1,track)+fiboDynRec(n-2,track)
        return track[n]
        
        

print(fibo_dynamique_iter(6))
print(fibo_dynamique_rec(6))
print(fibo_recursif(6))
