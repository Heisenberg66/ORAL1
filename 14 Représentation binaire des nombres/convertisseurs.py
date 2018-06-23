def decimal_to_binaire(n):
    bin=""
    while n>1:
        bin += str(n%2)
        n=n//2
    bin += str(n)
    return bin[::-1]
    

def binaire_to_decimal(bin):
    bin=bin[::-1]
    n=0
    for i in range(len(bin)):
        n+=int(bin[i])*2**i
    return n

def ABCDEF (i):
    if i<10:
        return str(i)
    if i==10:
        return "A"
    elif i==11:
        return "B"
    if i==12:
        return "C"
    elif i==13:
        return "D"  
    if i==14:
        return "E"
    elif i==15:
        return "F" 
        
                
def decimal_to_hexadecimal(n):
    hexa=""
    while n>15:
        hexa +=ABCDEF(n%16)
        n=n//16
    hexa +=ABCDEF(n)
    return hexa[::-1]
    
    
def hexa_to_decimal(hexa):
    n=0
    hexa = hexa[::-1]
    for i in range(len(hexa)):
        if hexa[i].isdigit():
            n+=int(hexa[i])*(16**i)
        else:
            n+=(ord(hexa[i])-55)*(16**i)
    return n
    
    
def binaire_to_hexadecimal(bin):
    if len(bin)>4:
        quatre="" #mot binaire de 4 bits
        hexa=""   
        i=len(bin)-1 # parcours à partir de la fin
        
        while i>=0:
            if len(quatre)==4:  # dès qu'on a un mot de 4 bit
                hexa+=ABCDEF(binaire_to_decimal(quatre[::-1])) # conversion en decimal entre 0 et 15 puis en chiffre ou lettre hexa
                quatre=""
            quatre+=bin[i]
            i-=1
            
        if len(quatre)>0:   # si il reste un mot binaire <4 bits non convertie
            hexa+=ABCDEF(binaire_to_decimal(quatre[::-1]))
        return hexa[::-1]
                
    
    return ABCDEF(binaire_to_decimal(bin))

def hexa_to_binaire(hexa):
    bin =""
    for c in hexa:
        bin +=decimal_to_binaire(hexa_to_decimal(c))
    return bin

# addition pour mot binaire de même longueur
def addition (bin1,bin2):
    bin1 = bin1[::-1]
    bin2= bin2[::-1]
    i=0
    retenu = 0 
    res = ""
    while i < len(bin1) and i <len(bin2):
        tmp = int(bin1[i])+int(bin2[i])+retenu
        if tmp ==0:
            retenu =0
            res+="0"
        elif tmp == 1:
            retenu = 0
            res+="1"
        elif tmp == 2:
            retenu = 1
            res+="0"
        else:
            retenu = 1
            res+="1"
        i+=1
    res+=str(retenu)
    return res[::-1]
            

print(decimal_to_binaire(91))
print(binaire_to_decimal("1011011"))
print(decimal_to_hexadecimal(91))
print(hexa_to_decimal("5B"))
print(binaire_to_hexadecimal("11101010"))
print(hexa_to_binaire("EA"))
print(addition("1011","1001"))