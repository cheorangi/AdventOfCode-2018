#read data from file or supply test input to list of claims

fabric = [[0 for i in range(1000)]for j in range(1000)]

claims = ["#1 @ 10,30: 40x40", "#2 @ 30,10: 40x40", "#3 @ 50,50: 20x20"]
'''with open('day3p1-curtis-input.txt') as infile:
    claims = infile.read().splitlines()'''

cleanedClaims = []

for i in claims:
    temp = i.split(' ')
    ID = temp[0][1:]
    x = temp[2].split(',')[0]
    y = temp[2].split(',')[1][:-1]
    width = temp[3].split('x')[0]
    height = temp[3].split('x')[1]
    result = ID + ' ' +  x  + ' ' + y + ' ' + width + ' ' + height
    cleanedClaims.append(result.split(' '))

usedfabric = set()

def markFabric(c):
    overlap = 0
    for y in range(int(c[2]), int(c[2]) + int(c[4])):
        for x in range(int(c[1]), int(c[1]) +int(c[3])):
            if (x,y) not in usedfabric:
                usedfabric.add((x,y))
            else:
                overlap += 1
    return overlap

def test(c):
    overlap = 0
    for i in range(int(c[3])):
        for j in range(int(c[4])):
            x = int(c[2]) + i
            y = int(c[3]) + j
            if fabric[y][x] == 0:
                fabric[y][x] = 1
            elif fabric[y][x] == 1:
                overlap += 1
                fabric[y][x] = 'x'
    return overlap

totalOverlap = 0
for i in cleanedClaims:
    totalOverlap += markFabric(i)


'''
#convert to use sets instead of lists
def createMatrix(c):
    matrix = []
    for y in range(int(c[2]), int(c[2]) + int(c[4])):
        row = set()
        for x in range(int(c[1]), int(c[1]) +int(c[3])):
            if (x,y) not in usedfabric:
                usedfabric.add((x,y))
            else:
                overlap += 1
            row.add((x, y))
        matrix.append(row)
    return matrix

def checkOverlap(m1, m2):
    count = 0
    if len(m1) <= len(m2):
        for i in range(len(m1)):
            r1 = m1[i]
            for j in range(len(m2)):
                r2 = m2[j]
                count += len(r1.intersection(r2))
    else:
        for i in range(len(m2)):
            r1 = m2[i]
            for j in range(len(m1)):
                r2 = m1[j]
                count += len(r1.intersection(r2))
    
    return count

test = 0

for i in range(len(cleanedClaims)):
    m1 = createMatrix(cleanedClaims[i])
    for j in range(i+1, len(cleanedClaims)):
        m2 = createMatrix(cleanedClaims[j])
        test += checkOverlap(m1, m2)
'''

print(totalOverlap)