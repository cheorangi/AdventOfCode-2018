#getting started on day 3 this one is gonna be a doozy
from math import sqrt

#claims = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
with open('day3p1-curtis-input.txt') as infile:
    claims = infile.read().splitlines()

fabric = (1000,1000)

def splitClaim(c):
    _id = c.split(' ')[0][-1]
    _coord = c.split(' ')[2][:-1].split(',')
    _size = c.split(' ')[3].split('x')
    return _id, _coord, _size


def checkOverlap(c1, c2):
    c1Id, c1Coord, c1Size = splitClaim(c1)
    c2Id, c2Coord, c2Size = splitClaim(c2)

    #if any part of the rectangle is between the left x and right side x
    if c1Coord[0] > c2Coord[0] + c2Size[0] or c1Coord[0] + c1Size[0] > c2Coord[0]:
        return False
    
    if c1Coord[1] < c2Coord[1] + c2Size[1] or c1Coord[1] + c1Size[1] < c2Coord[1]:
        return False

    return True

def calcOverlap(c1, c2):
    c1Id, c1Coord, c1Size = splitClaim(c1)
    c2Id, c2Coord, c2Size = splitClaim(c2)

    a1 = abs(int(c1Coord[0]) - int(c1Coord[0]) + int(c1Size[0])) * abs(int(c1Coord[1]) - int(c1Coord[1]) + int(c1Size[1]))

    a2 = abs(int(c2Coord[0]) - int(c2Coord[0]) + int(c2Size[0])) * abs(int(c2Coord[1]) - int(c2Coord[1]) + int(c2Size[1]))

    aI = (min(int(c1Coord[0]) + int(c1Size[0]), int(c2Coord[0]) + int(c2Size[0])) - max(int(c1Coord[0]), int(c1Coord[0]) + int(c1Size[0]))) * (min(int(c1Coord[1]) + int(c1Size[1]), int(c2Coord[1]) + int(c2Size[1])) - max(int(c1Coord[1]), int(c1Coord[1]) + int(c1Size[1])))

    return (a1 + a2 - aI)

totalOverlap = 0
for i in range(len(claims)-1):
    for j in range(i+1, len(claims)):
        if (checkOverlap(claims[i], claims[j])):
            print('Claims overlap')
            totalOverlap += calcOverlap(claims[i], claims[j])
        else:
            print('No Claims Overlap')

print(totalOverlap)
