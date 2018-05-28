import random as random



def six_en_4_lancers():
    six = 0
    for _ in range(4):
        r = random.randint(1,6)
        if r == 6:
            six+=1
    return six >= 1


def quatre_6_en_24_lancers():
    double_six = 0
    for _ in range(24):
        r = random.randint(1,6)
        r1 = random.randint(1,6)
        if r == 6 and r1==6:
            double_six+=1
    return double_six >= 1
    
def simulation (n):
    simple = 0
    double = 0
    for _ in range(n):
        if six_en_4_lancers():
            simple+=1
        if quatre_6_en_24_lancers():
            double+=1
    return simple/n,double/n


print(simulation(10000))