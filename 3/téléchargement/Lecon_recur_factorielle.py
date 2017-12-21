def facto(n):
    if n == 0:                        # Cas de base
        return 1
    return n * facto(n-1)        # Appel récursif 
    
    
print(facto(4))

###

|-- facto(4)
|  |-- facto(3)
|  |  |-- facto(2)
|  |  |  |-- facto(1)
|  |  |  |  |-- facto(0)
|  |  |  |  |  |-- return 1
|  |  |  |  |-- return 1
|  |  |  |-- return 2
|  |  |-- return 6
|  |-- return 24
24 
###