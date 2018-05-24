
def syracuse_suivant(n):
    if (n%2 == 0):
        return n // 2
    else:
        return 3*n + 1

def syracuse_liste(n):
    print(n)
    etape = 0
    while (n != 1):
        n = syracuse_suivant(n)
        etape += 1
        print(n)
    print(str(etape)+" etapes")

syracuse_liste(27)