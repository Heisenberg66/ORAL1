def est_delimiteur(chara):
    if chara==' ' or chara=='\t' or chara =='\n':
        return True
    return False


def word_count (filename):
    
    file = open(filename)
    nb_line,nb_word,nb_char =0,0,0
    char_precedent='a' 
    for line in file:
        nb_line+=1
        for char in line:
            nb_char+=1
            if not est_delimiteur(char) and est_delimiteur(char_precedent):
                nb_word+=1
            
            char_precedent=char
    
    file.close()
    return (nb_line,nb_word,nb_char)



print(word_count("man.txt"))