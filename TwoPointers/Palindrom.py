s = 'A man, a plan, a canal: Panama'

def Palindrom(s):
    s = s.replace(',',' ').replace('.',' ').replace(';',' ').replace(':',' ')
    s = s.replace(' ','')
    s = s.lower()
    return s == s[::-1]

print(Palindrom(s))
