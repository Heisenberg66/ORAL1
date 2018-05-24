    
def tri_inser(l):

    for i in range(1,len(l)):
        tmp=l[i]
        j=i
        while j>0 and tmp<l[j-1]:
            l[j]=l[j-1]
            j-=1
        l[j]=tmp
 
liste = [3,56,47,39,82,2,0,40,23]
tri_inser(liste)
print(liste)