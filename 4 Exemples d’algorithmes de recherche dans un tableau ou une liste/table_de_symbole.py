from collections.abc import MutableMapping
import string
import time

class LinkedST(MutableMapping):
    
    class Node:
        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next
            
        def __str__(self):
            return str(self.key) + ': ' + str(self.value)
            
    def __init__(self):
        self.first = None
        self.length = 0
    
    def __len__(self):
        return self.length
        
    def __str__(self):
        return " -> ".join((str(k) + ": " + str(self[k])) for k in self)
    
    def __iter__(self):
        node = self.first
        while node is not None:
            yield node.key
            node = node.next
    
    def __setitem__(self, key, value):
        node = self.first
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next
        self.first = LinkedST.Node(key, value, self.first)
        self.length += 1

    def __delitem__(self, key):
        node = self.first
        if node is None:
            raise KeyError
        if node.key == key:
            self.first = node.next
            self.length -= 1
            return
        while node.next is not None:
            if node.next.key == key:
                node.next = node.next.next
                self.length -= 1
                return
            node = node.next
        raise KeyError(key)

    def __getitem__(self, key):
        node = self.first
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError(key)
        
        

class hash_table(MutableMapping):
    
    def __init__(self,N):
        self.table= [LinkedST() for _ in range(N)]
        self.longueur=N
        
    def __len__(self):
        return self.nbelem
        
    def __iter__(self):
        for lst in self.table:    
            yield from lst
        
        
    def __str__(self):
        stri=""
        i=0
        for lst in self.table:
            stri+=str(i)+" : "
            for elem in lst:
                stri+=elem+" ; "
            i+=1
            stri+="\n"
        return stri
                
                
        
    
    def __setitem__(self, key, value):
        h=hash(key)%self.longueur
        self.table[h][key]=value
                
    def __delitem__(self, key):
        h=hash(key)%self.longueur
        del self.table[h][key]
        
    def __getitem__(self, key):
        h=hash(key)%self.longueur
        return self.table[h][key]
        
    
if __name__ == "__main__":
   
    ht = hash_table(5000)
    
    file = open('sense_and_sensibility.txt', 'r',encoding="utf-8")
    text=file.read()
    replace_punctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    text = text.translate(replace_punctuation)
    
    with open('sense_and_sensibility_wo_punct.txt', 'a',encoding="utf-8") as the_file:
        the_file.write(text)
    
    
    with open('sense_and_sensibility_wo_punct.txt','r',encoding="utf-8") as f:
        t_start=time.time()
        for line in f:
            for word in line.split():
                ht[word]=ht.get(word,0)+1
        print(time.time()-t_start)
    
    
    
    
    
    # t = LinkedST()
    # for i, c in enumerate('EXAMPLE'):
    #     t[c] = i
    # print(t.items)
    # print(len(t))
    # for k in t:
    #     print(k, ": ", t[k])
