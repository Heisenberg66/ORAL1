def fibo1(n):
    if n <0 : 
        return "Error"
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b 



def fibo2(n):
    if n <0 : 
        return "Error"
    if n < 2:
        return 1
    return fibo2(n-1) + fibo2(n-2) 



def fibo3(n):
    if n <0 : 
        return "Error"
        
    def moteur(k, a,b):
        if k == 0:
            return a
        return moteur(k - 1, b, a + b)
    return moteur(n, 1, 1) 
    
    
    
print(fibo1(6))
print(fibo2(6))
print(fibo3(6))

    ### pile d'exececution pour la dernier fonction ! 

|-- moteur(6, 1, 1)
|  |-- moteur(5, 1, 2)
|  |  |-- moteur(4, 2, 3)
|  |  |  |-- moteur(3, 3, 5)
|  |  |  |  |-- moteur(2, 5, 8)
|  |  |  |  |  |-- moteur(1, 8, 13)
|  |  |  |  |  |  |-- moteur(0, 13, 21)
|  |  |  |  |  |  |  |-- return 13
|  |  |  |  |  |  |-- return 13
|  |  |  |  |  |-- return 13
|  |  |  |  |-- return 13
|  |  |  |-- return 13
|  |  |-- return 13
|  |-- return 13
13 
    
    