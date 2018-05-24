def tri_bulle(l):
     
     for i in range (0,len(l)-1):
         for j in range (i+1,len(l)):
             if l[i]>l[j]:
                 l[i],l[j] = l[j],l[i]


liste = [3,56,47,39,82,2,0,40,23]
tri_bulle(liste)
print(liste)