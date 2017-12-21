def puissance_naive(x, n):
    """Version récursive"""
    if n == 0:
        return 1
    return x * puissance_naive(x, n - 1) 
    
    

def puissance_rapide(x, n):
    """ Version récursive"""
    if  n == 0:
        return 1
    nombre = puissance_rapide(x, n // 2)
    if n % 2 == 0:
        return nombre * nombre
    return x * nombre * nombre

# print(puissance_naive(2,10))
# print(puissance_rapide(2,10))

### Exemple d'éxécution
|-- puissance_rapide(3, 11)
|  |-- puissance_rapide(3, 5)
|  |  |-- puissance_rapide(3, 2)
|  |  |  |-- puissance_rapide(3, 1)
|  |  |  |  |-- puissance_rapide(3, 0)
|  |  |  |  |  |-- return 1
|  |  |  |  |-- return 3
|  |  |  |-- return 9
|  |  |-- return 243
|  |-- return 177147
177147 
###