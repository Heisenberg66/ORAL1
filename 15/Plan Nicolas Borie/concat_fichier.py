f = open("foo", "r")
g = open("bar", "r")
h = open("result", "w")

def concat_fichier(f, g, h):
#    for line in f:
#        h.write(line)
#    for line in g:
#        h.write(line)
    h.write(f.read())
    h.write(g.read())

concat_fichier(f, g, h)

f.close()
g.close()
h.close()