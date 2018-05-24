def pgcd(a, b):
    if b == 0:
        return a
    return pgcd(b, a % b) 
    
    
#### Exemple d'éxécution
|-- pgcd(1234567, 7654321)
|  |-- pgcd(7654321, 1234567)
|  |  |-- pgcd(1234567, 246919)
|  |  |  |-- pgcd(246919, 246891)
|  |  |  |  |-- pgcd(246891, 28)
|  |  |  |  |  |-- pgcd(28, 15)
|  |  |  |  |  |  |-- pgcd(15, 13)
|  |  |  |  |  |  |  |-- pgcd(13, 2)
|  |  |  |  |  |  |  |  |-- pgcd(2, 1)
|  |  |  |  |  |  |  |  |  |-- pgcd(1, 0)
|  |  |  |  |  |  |  |  |  |  |-- return 1
|  |  |  |  |  |  |  |  |  |-- return 1
|  |  |  |  |  |  |  |  |-- return 1
|  |  |  |  |  |  |  |-- return 1
|  |  |  |  |  |  |-- return 1
|  |  |  |  |  |-- return 1
|  |  |  |  |-- return 1
|  |  |  |-- return 1
|  |  |-- return 1
|  |-- return 1
1 
###