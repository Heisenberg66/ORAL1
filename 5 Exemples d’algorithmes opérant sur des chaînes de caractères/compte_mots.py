
def compte_mots(chaine):
    mot = 0
    for i in range(0,len(chaine)-1):
        courant = chaine[i]
        suivant = chaine[i+1]
        #le couractère courant est un espace mais pas le suivant
        #ou on arrive à la fin de la chaine et le dernier caractère
        if (not courant.isspace() and suivant.isspace()) or (i == len(chaine)-2 and not suivant.isspace()) :
             mot+=1
    return mot
    
print(compte_mots("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vestibulum justo a nisi pretium imperdiet. Aenean aliquet velit."))
    
    