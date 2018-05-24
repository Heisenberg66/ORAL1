# Methode pour calculer une racine carree...

def racine(n, prec):
    grand_pere = n/2.0
    pere = 2.0 
    while (abs(grand_pere - pere) > prec):
        print(pere)
        fils = (grand_pere + pere) / 2.0
        grand_pere = fils
        pere = n / grand_pere
    return pere
    
print(racine(40000000000, 0.000000001))