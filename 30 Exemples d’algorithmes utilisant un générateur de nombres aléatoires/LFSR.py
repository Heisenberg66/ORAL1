class LFSR:
    def __str__(self):
        return format(self.state,'0'+str(self.m)+'b')
    
    def __init__(self,state,m,taps):
        """
        :arg m: nombre de bits du générateur
        :arg state: un entier entre 1 et 2^m-1, l'état initial
        :arg taps: un tuple d'indices (entre 0, tout à droite, et m-1 à gauche)
           indiquant les cases où on fait agir la rétroaction
        """
        # FIXME
        
        self.state=state
        self.m=m
        self.taps=taps
        
        
    def step(self):
        """Fait un pas du LFSR, renvoie le bit de sortie"""
        # FIXME
        # decalage à gauche 
        decalage = self.state<<1
        
        # extraction du bit de poids fort
        exit_bit = decalage>>(self.m)
                        
        if exit_bit == 1:
            
            # decalage - bit de poids fort
            decalage = decalage - (2**self.m)
            
            # construction du mot binaire pour XOR
            mot_bin = 0
            for i in range(self.taps[0],self.taps[1]+1):
            	mot_bin += 2**i

            # XOR
            decalage= decalage^mot_bin
        
        self.state = decalage
        return exit_bit
        
    
    def periode(self):
        lst= []
        s = format(self.state,'0'+str(self.m)+'b')

        while s not in lst:
            lst.append(s)
            self.step()
            s = format(self.state,'0'+str(self.m)+'b')

        return len(lst)
            
        



class Encrypter:
    def __init__(self,m,taps):
        # à coder  
        self.lfsr = LFSR(4,m,taps)
        
    def encrypt_integer(self,i):
        # chiffre un entier
        s=""
        for _ in range(7):
            s+=str(self.lfsr.step())
        return i^(int(s,2)) 
        
    def encrypt_integer_list(self,lst):
        # chiffre une liste d'entiers
        res_lst = list()
        for integ in lst:
            res_lst.append(self.encrypt_integer(integ))
        return res_lst
            
    def encrypt_string(self,chaine,mot_de_passe):
        # chiffre une chaîne de caractères avec le mot de passe donné
        self.lfsr.state=mot_de_passe
        lst = encode(chaine)
        return self.encrypt_integer_list(lst)
            
    def decrypt_list(self,liste,mot_de_passe):
        # déchiffre une liste d'entiers avec le mot de passe donné
        res = ""
        self.lfsr.state=mot_de_passe
        
        for integ in liste :
            s=""
            for _ in range(7):
                s+=str(self.lfsr.step())
            masque = int(s,2)
            res+= chr(integ^masque)
        return res
        
        

def encode(s):
    
    return list(s.encode("ascii"))

def decode(lst):
    
    for i in range(len(lst)):
        lst[i]= chr(lst[i])
    return "".join(lst)
    


# lfsr = LFSR(11,4,(0,1))
# print(lfsr.periode())
# lst= []
# s = str(lfsr)
# 
# while s not in lst:
#     lst.append(s)
#     lfsr.step()
#     s = str(lfsr)
# 
# print(lst)

# une seul valeur possible (0) si on initialise à 0

# pour des taps de 0 à 2, on obtient moins de valeurs ;  7 au lieu de 15 

# print(decode([67, 39, 101, 115, 116, 32, 98, 111, 110, 32, 33]))
# 
# print(decode(encode("Ca marche !")))

cryptor = Encrypter(4,(0,1))
print(cryptor.decrypt_list([28,124,65,99,56,49,25],10))
print(cryptor.decrypt_list(cryptor.encrypt_string("Salut les aminches !",10),10))




message = [5, 17, 79, 33, 113, 42, 50, 0, 19, 58, 18, 68, 55, 62, 32, 119, 0, 3, 37, 17, 85, 44, 113, 41, 50, 7, 21, 119, 4, 78, 42, 62, 46, 127, 30, 9, 37, 4, 64, 43, 106, 103, 102, 1, 70, 53, 21, 1, 41, 123, 33, 102, 78, 18, 56, 80, 66, 45, 127, 41, 113, 11, 72, 119, 93, 12, 101, 76, 105, 50, 45, 9, 33, 21, 88, 42, 107]
cryptor = Encrypter(6,(0,1))
print(cryptor.decrypt_list(message,42))

