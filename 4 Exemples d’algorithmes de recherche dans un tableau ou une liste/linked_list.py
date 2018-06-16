


#-------------------------------------------------------------------------------

class Maillon:
    
    def __init__(self,value, suivant=None):
        self.value=value
        self.suivant=suivant

#-------------------------------------------------------------------------------

class Linked_List:
    
    # constructeur
    def __init__(self,premier=None):
        self.premier=premier
        self.taille= 0
        if self.premier is not None:
            self.taille+= 1
    # renvoie la longueur de la liste        
    def __len__(self):
        return self.taille
    
    # renvoie un string de la liste
    def __str__(self):
        courant = self.premier
        s = "["
        while courant is not None:
            s+=str(courant.value)+", "
            courant = courant.suivant
        return s+"]"
        
    # ajoute un élément à la fin de la liste
    # Complexité : O(n)
    def append(self,val):
        if self.premier is None:
            self.premier = Maillon(val,None)
        else:
            courant = self.premier
            while courant.suivant is not None:
                courant = courant.suivant
            courant.suivant = Maillon(val,None)
        
        self.taille+=1 
        
    # ajoute un élément au début de la liste
    # Complexité : O(1)
    
    def append_debut(self,val):
        if self.premier is None:
            self.premier = Maillon(val,None)
        else:
            old_premier = self.premier
            self.premier = Maillon(val,old_premier)
        self.taille+=1

        
# ------------------------------------------------------------------------------
# -------------------- Algorithme sur liste non triée --------------------------
# ------------------------------------------------------------------------------

    
    # renvoie True si l'objet appartient à la liste, False si non
    # Complexité : O(i)
    def est_present(self,val):
        courant = self.premier
        while courant is not None:
            if courant.value == val:
                return True
            courant = courant.suivant
        return False

# ------------------------------------------------------------------------------

    
    # renvoie la postion d'une objet dans la liste
    # complexité : O(i)
    def position(self,val):
        courant = self.premier
        pos =0
        while courant is not None:
            if courant.value == val:
                return pos
            courant = courant.suivant
            pos+=1
        return -1
        
# ------------------------------------------------------------------------------

        
    # renvoie l'élément à la position i
    # Complexité : O(i)
    def a_la_position(self,i):
        if i >self.taille-1:
            return "index out of range"
        else:
            courant = self.premier
            pos =0
            while pos<i:
                courant = courant.suivant
                pos+=1
            return courant.value
            
# ------------------------------------------------------------------------------

            
    # renvoie le nombre d'occurence d'un objet
    # complexité : O(n)
    def occurence (self,val):
        occ = 0
        courant= self.premier
        while courant is not None:
            if courant.value== val:
                occ+=1
            courant= courant.suivant
        return occ


# ------------------------------------------------------------------------------


    # renvoie la postion des doublons d'un objet
    # Complexité : O(n)
    def doublon (self,val):
        pos = []
        i=0
        courant= self.premier
        while courant is not None:
            if courant.value== val:
                pos.append(i)
            courant= courant.suivant
            i+=1
        return pos


# ------------------------------------------------------------------------------

        
    # renvoie le minimum d'un tableau ( éléments comparables)
    # Complexité : O(n
    def min (self):
        courant = self.premier
        if courant is not None:
            min = self.premier.value
            courant = courant.suivant
            while courant is not None:
                if courant.value<min:
                    min = courant.value
                courant = courant.suivant
            return min
        else:
            return None

    
# ------------------------------------------------------------------------------

    
    # renvoie le maximum d'un tableau ( éléments comparables)
    # Complexité : O(n
    def max (self):
        courant = self.premier
        if courant is not None:
            max = self.premier.value
            courant = courant.suivant
            while courant is not None:
                if courant.value>max:
                    max = courant.value
                courant = courant.suivant
            return max
        else:
            return None
 
 
#-------------------------- Recherche auto adaptative --------------------------
    
    # recherche auto adaptive, avancé l'élement de 1
    # on ne va pas redefinir tous les pointeurs, on va juste inverser les valeurs
    # des maillons courant et courant.suivant
    def auto_methode1(self,val):
        if self.premier is not None and self.premier.suivant is not None \
        and self.premier.value!=val:
            courant=self.premier
            while courant.suivant is not None:
                if courant.suivant.value == val:
                    courant.value,courant.suivant.value = courant.suivant.value,courant.value
                courant =courant.suivant
                    
            
    # recherche auto adaptive, on place l'élément en tête de liste
    def auto_methode2(self,val):
        if self.premier is not None and self.premier.suivant is not None \
        and self.premier.value!=val:
            courant=self.premier
            while courant is not None and courant.suivant is not None:
                if courant.suivant.value == val:
                    old = courant.suivant
                    courant.suivant = courant.suivant.suivant
                    old.suivant=self.premier
                    self.premier=old
                    
                courant =courant.suivant


#-------------------------------------------------------------------------------
# ----------------- Algorithmes pour liste triée --------------------------
#-------------------------------------------------------------------------------


    # verifie si la valeur est dans la liste
    # s'arrète quand l[i] > val
    def est_present2(self,val):
        courant=self.premier
        while courant is not None and courant.value <=val:
            if courant.value == val:
                return True
            courant=courant.suivant
        return False
    
    
    # ------------------------------------------------------------------------------
    
    
    # renvoie la position de la valeur si elle est dans le tableau
    def position2(self,value):
        courant=self.premier
        i=0
        while courant is not None and courant.value <=val:
            if courant.value == val:
                return i
            courant=courant.suivant
            i+=1
        return -1
    
    # ------------------------------------------------------------------------------   
    # "a_la_position" reste la même méthode
    # ------------------------------------------------------------------------------
    
    
    # occurence2 n'a pas besoin de parcourir toute la liste
    def occurence2 (self,val):
        courant=self.premier
        occ=0
        while courant is not None and courant.value <=val:
            if courant.value == val:
                occ+=1
            courant=courant.suivant
        return occ
    
    
    # ------------------------------------------------------------------------------
    
    
    # doublons2  n'a pas besoin de parcourir toute la liste
    def doublons2 (self,val):
        courant=self.premier
        doublon = []
        i=0
        while courant is not None and courant.value <=val:
            if courant.value == val:
                doublon.append(i)
            courant=courant.suivant
            i+=1
        return doublon
        
    
    # ------------------------------------------------------------------------------
    
    
    # renvoie la valeur du premier élément
    def min2 (self):
        return self.premier.value
    
    
    # ------------------------------------------------------------------------------
    
    
    # renvoie la valeur du dernier élément    
    def max2(self):
        if self.premier is not None:
            courant = self.premier
            while courant.suivant is not None:
                courant = courant.suivant
            return courant.value
        return None
        
        
#-------------------------------------------------------------------------------            
#---------------------------------- MAIN ---------------------------------------
#-------------------------------------------------------------------------------    

if __name__ == "__main__":
    l = Linked_List(Maillon(1,Maillon(3,Maillon (3, Maillon (7,None)))))
    l.taille = 4
    print(l)
    print(l.min2())
    