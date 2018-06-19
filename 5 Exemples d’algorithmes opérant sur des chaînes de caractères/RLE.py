import random as r

def RLE (chaine):
    output = ""
    courant = chaine[0]
    nb=0 
    for char in chaine:
        print(char)
        if courant == char:
            nb+=1
        else:
            output= output+str(nb)+courant
            courant=char
            nb=1
    return output+str(nb)+courant

s= "aaabccccddeee"
print(RLE(s))


print(r.shuffle(list(range(10))))