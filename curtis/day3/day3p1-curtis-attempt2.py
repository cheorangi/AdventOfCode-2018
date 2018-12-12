#getting started on day 3 this one is gonna be a doozy
from math import sqrt
import re

#claims = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
with open('day3p1-curtis-input.txt') as infile:
    claims = infile.read().splitlines()
    '''for r in infile.readlines():
        r = re.split('[^0-9]+', r[1:].strip())
        claims.append([int(d) for d in r])'''

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

#convert to use sets instead
def createMatrix(c):
    matrix = []
    for y in range(int(c[2]), int(c[2]) + int(c[4])):
        row = set()
        for x in range(int(c[1]), int(c[1]) +int(c[3])):
            row.add((x, y))
        matrix.append(row)
    return matrix

def checkOverlap(m1, m2):
    count = 0
    if len(m1) < len(m2):
        for i in range(len(m1)):
            r1 = m1[i]
            r2 = m2[i]
            temp = r1.intersection(r2)
            count += len(temp)
    else:
        for i in range(len(m2)):
            r1 = m2[i]
            r2 = m1[i]
            temp = r1.intersection(r2)
            count += len(temp)
    
    return count

overlap = 0

print(len(cleanedClaims))

for i in range(len(cleanedClaims)):
    m1 = createMatrix(cleanedClaims[i])
    for j in range(i+1, len(cleanedClaims)):
        m2 = createMatrix(cleanedClaims[j])
        overlap += checkOverlap(m1, m2)

print(overlap)
'''
for i in range(len(claimsMatrices)):
    for j in range(i+1, len(claimsMatrices)):
       overlap += checkOverlap(claimsMatrices[i], claimsMatrices[j])
'''
