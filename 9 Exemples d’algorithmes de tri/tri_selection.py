def tri_select(l):
    
    for i in range(len(l)):
        indice = i
        min = l[i]
        for j in range(i+1,len(l)):
            if l[j]<min:
                
                min = l[j]
                indice = j
        
        l[indice] = l[i]
        l[i] = min


liste = [3,56,47,39,82,2,0,40,23]
tri_select(liste)
print(liste)