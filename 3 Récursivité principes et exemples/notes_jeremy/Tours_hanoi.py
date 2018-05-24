def hanoi(n):
    """ Déplacement solution de T1 vers T3 pour les tours de Hanoi"""
    sol = []
    def moteur(k, a, b, c):
        if k == 0:
            return
        else:
            moteur(k - 1, a, c, b)
            sol.append((a,c))
            moteur(k - 1, b, a, c)
    moteur(n, 1, 2, 3)
    return sol

print(hanoi(4))

[(1, 2), (1, 3), (2, 3), (1, 2), (3, 1), (3, 2), (1, 2), (1, 3), (2, 3), (2, 1), (3, 1), (2, 3), (1, 2), (1, 3), (2, 3)] 

