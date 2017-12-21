def rech_dicho(tab, elem):
    """ Position de elem dans la liste triée tab (-1 si elem n'y est pas)"""
    def moteur(deb, fin):
        """ moteur de recherche dichotomique récursif"""
        if deb > fin:
            return -1
        milieu = (deb + fin) // 2
        m = tab[milieu]
        if elem < m:
            return moteur(deb,milieu - 1)
        if elem > m:
            return moteur(milieu + 1, fin)
        return milieu
    return moteur(0, len(tab) - 1)
    
    
# print(rech_dicho([1,2,3,4,5,5,5,5,5,5,5,5],5))

#####
t = [1,3,5,6,6,8,9,14,15]
print(rech_dicho(t, 7))
print(rech_dicho(t, 14))

def rech_dicho(tab, elem):
    """ Position de elem dans la liste triée tab (-1 si elem n'y est pas)"""
    def moteur(deb, fin):
        """ moteur de recherche dichotomique récursif"""
        if deb > fin:
            return -1
        milieu = (deb + fin) // 2
        m = tab[milieu]
        if elem < m:
            return moteur(deb,milieu - 1)
        if elem > m:
            return moteur(milieu + 1, fin)
        return milieu
    return moteur(0, len(tab) - 1)
    
    
|-- moteur(0, 8)
|  |-- moteur(5, 8)
|  |  |-- moteur(5, 5)
|  |  |  |-- moteur(5, 4)
|  |  |  |  |-- return -1
|  |  |  |-- return -1
|  |  |-- return -1
|  |-- return -1
-1
|-- moteur(0, 8)
|  |-- moteur(5, 8)
|  |  |-- moteur(7, 8)
|  |  |  |-- return 7
|  |  |-- return 7
|  |-- return 7
7 