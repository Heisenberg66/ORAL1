def fibo(n):
    if n <0 :              #Cas d'erreur
        print("SyntaxError: Invalid syntax") 
        return None
    if n < 2:              #Cas d'arret
        return 1
    return fibo(n-1) + fibo(n-2) 
    
print(fibo(-4))