ids = ['abcde', 'fghij', 'klmno', 'pqrst',  'fguij' ,'axcye', 'wvxyz']

def match(s1, s2):
    pos = -1

    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i
    return pos

for i in range(len(ids)-1):
    for j in range(len(ids)-1):
        pos = match(ids[i], ids[j+1])

print(pos)