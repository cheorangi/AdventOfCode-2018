#getting started on day 3 this one is gonna be a doozy
from math import sqrt
import re

#claims = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
with open('day3p1-curtis-input.txt') as infile:
    claims = infile.read().splitlines()
    '''for r in infile.readlines():
        r = re.split('[^0-9]+', r[1:].strip())
        claims.append([int(d) for d in r])'''

print(claims[0])

cleanedClaims = []

for i in claims:
    temp = i.split(' ')
    ID = temp[0][1:]
    x = temp[2].split(',')[0]
    y = temp[2].split(',')[1][:1]
    width = temp[3].split('x')[0]
    height = temp[3].split('x')[1]
    result = ID + ' ' +  x  + ' ' + y + ' ' + width + ' ' + height
    cleanedClaims.append(result.split(' '))

print(cleanedClaims)


def createMatrix(c):
    matrix = []
    for y in range(int(c[2]), int(c[2]) + int(c[4])):
        row = []
        for x in range(int(c[1]), int(c[1]) +int(c[3])):
            row.append((x, y))
        matrix.append(row)
    return matrix

def checkOverlap(m1, m2):
    count = 0
    for i in m1:
        for j in i:
            for k in m2:
                if j in k:
                    count += 1
    
    return count

overlap = 0

for i in range(len(cleanedClaims)):
    #print('checking claim: ' + cleanedClaims[i][0])
    #print(cleanedClaims[i])
    m1 = createMatrix(cleanedClaims[i])
    for j in range(i+1, len(cleanedClaims)):
        #print(cleanedClaims[j])
        m2 = createMatrix(cleanedClaims[j])
        overlap += checkOverlap(m1, m2)


print(overlap)
'''
for i in range(len(claimsMatrices)):
    for j in range(i+1, len(claimsMatrices)):
       overlap += checkOverlap(claimsMatrices[i], claimsMatrices[j])
'''
