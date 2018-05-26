def AND(a,b):
    if a==1:
        if b==1:
            return 1
    return 0
    
def OR(a,b):
    if a==1:
        return 1
    if b==1:
        return 1
    if AND(a,b)==1:
        return 1
    return 0

def NON(a):
    if a ==1:
        return 0
    return 1

    
def NOR(a,b):
    return NON(OR(a,b))
    
def NAND(a,b):
    return NON(AND(a,b))


def XOR (a,b):
    if a==1:
        if b==1:
            return 0
        return 1
    elif a==0:
        if b==1:
            return 1
    return 0
    
def operation (a,b,c):
    return OR((AND(AND(a,b),NON(c))),AND(NON(a),c))
    
print("A | B | C | D")
for a in range(0,2):
    for b in range (0,2):
        for c in range (0,2):
            print(str(a)+" | "+str(b)+" | "+str(c)+" | "+str(operation(a,b,c)))
            


