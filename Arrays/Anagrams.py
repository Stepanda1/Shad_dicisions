s = 'мука'
t = 'кумы'

def Anagrams(s,t):
    if len(s) != len(t):
        return False
    sort_s = sorted(s)
    sort_t = sorted(t)
    if sort_s == sort_t:
        return True
    else:
        return False
    
print(Anagrams(s,t))