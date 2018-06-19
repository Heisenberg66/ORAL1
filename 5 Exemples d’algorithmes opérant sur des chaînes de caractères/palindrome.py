def palindrome (s):
    debut = 0
    fin = len(s)-1
    while fin - debut >=0:
        if s[fin]!=s[debut]:
            return False
        debut+=1
        fin-=1
    return True
    

print(palindrome("Bob"))
    