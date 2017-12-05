def fusion(t1,t2):
    
    i1,i2,n1,n2=0,0,len(t1),len(t2)
    t=[] 
    
    while i1<n1 and i2<n2:
        if t1[i1]<t2[i2]:
            t.append(t1[i1])
            i1+=1
        else:
            t.append(t2[i2])
            i2+=1
    if i1==n1:
        t.extend(t2[i2:])
    else:
        t.extend(t1[i1:])
        
    return t
        


def tri_fusion(t):
    if len(t)<2:
        return t
    else:
        m=len(t)//2
        return fusion(tri_fusion(t[:m]),tri_fusion(t[m:]))
        
        
liste = [3,56,47,39,82,2,0,40,23]
print(tri_fusion(liste))
