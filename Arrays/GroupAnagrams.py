strs = ['eat','tea','ate','tan', 'ate', 'nat', 'bat']

def GroupAnagrams(strs):
    d = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in d:
            d[key].append(s)
        else:
            d[key] = [s]
    return list(d.values())

print(GroupAnagrams(strs))