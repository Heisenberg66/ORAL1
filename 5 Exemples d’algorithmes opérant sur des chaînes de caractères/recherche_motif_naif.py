# recherche naive dans une chaine de caracteres
# Complexité O(nm)
def recherche_motif_naif(chaine,pattern):
    pos = []
    if len(pattern)<=len(chaine):
        for i in range(len(chaine)-len(pattern)+1):
            j=0
            while j<len(pattern):
                if pattern[j]!=chaine[j+i]:
                    break
                j+=1
            else:
                pos.append(i)
    return pos
    

c="ABCDEFGHABCTHABC"
p="HA"
print(recherche_motif_naif(c,p))