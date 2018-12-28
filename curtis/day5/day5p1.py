#example = 'dabAcCaCBAcCcaDA'

example = open('input.txt').read()
#print(example)

def removePairs(s):
    temp = None
    for i in range(len(s)-1):
        c1 = s[i]
        c2 = s[i+1]
        if c1 == c2.lower() or c1.lower() == c2 or c1 == c2.upper() or c1.upper() == c2:
            temp = s[:i] + s[i+2:]
            return temp
    if temp == None:
        return s

currString = example
cont = True
while cont:
    if currString == removePairs(currString):
        cont = False
    else:
        currString = removePairs(currString)

print('Answer Part 1: {}'.format(len(currString)))
