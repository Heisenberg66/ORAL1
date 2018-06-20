def euclide_iter(a,b):
    while a%b!=0:
        a,b=b,a%b
    return b
    
def euclide_rec(a,b):
    if a%b!=0:
        return euclide_rec(b,a%b)
    return b
    
print(euclide_iter(96,76))
print(euclide_rec(96,76))
