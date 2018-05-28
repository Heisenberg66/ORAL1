print("Choisis un nombre entre 1 et 50 inclus")
inp = ""
while inp!="ok":
    inp = input("Tapes 'ok' quand tu es prêt : \n")

print("Je vais devinez ton nombre ... tapes : \n \t - : si le nombre est plus petit\n\t + : si le nombre est plus grand\n\t = : si j'ai trouvé")
min = 1 
max =50
while inp != "=":
    mid = (min+max)//2
    inp=input("Est-ce "+str(mid)+" ?\n")
    if inp=="+":
        min=mid
    elif inp == "-":
        max=mid
        
print("Je suis trop fort")
    