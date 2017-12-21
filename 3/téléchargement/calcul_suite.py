"Trois fonctions pour calculer u_n"
def u1(n):
    "Version itérative"
    u = 2
    for i in range(n):
        u = 0.5 * (u + 1 / u)
    return u 

def u2(n):
    "Version récursive naturelle"
    if n <0 : 
        return "Error"
    if n == 0:
        return 2
    return 0.5 * (u2(n - 1) + 1 / u2(n - 1)) 

def u3(n):
    "Version récursive complexe
    if n == 0:
        return 2
    x = u3(n-1)
    return 0.5 * (x + 1 / x) 
    
    
print(u1(-1))
print(u2(-1))
print(u3(0))
