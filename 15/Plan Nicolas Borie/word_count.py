def est_delimiteur(c):
    if c == ' ' or c == '\t' or c == '\n':
        return True
    return False

def word_count(fichier):
    f = open(fichier, "r")
    nb_ligne = 0
    nb_char = 0
    nb_mot = 0
    char_precedant = 'a'
    for ligne in f:
        nb_ligne += 1
        for caractere in ligne:
            nb_char += 1
            if est_delimiteur(char_precedant) and not est_delimiteur(caractere):
                nb_mot += 1
            char_precedant = caractere
    print("le fichier", fichier, "contient :")
    print(str(nb_ligne), " lignes")
    print(str(nb_mot), " mots")
    print(str(nb_char), " caracteres")
    
word_count("test")