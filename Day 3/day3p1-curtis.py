#getting started on day 3 this one is gonna be a doozy
'''class Claims():
    def __init__(self, xCoord, yCorrd, ):
        self.x ='''

claims = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

fabric = (1000,1000)

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle():
    def __init__(self, )

def splitClaim(c):
    _id = c.split(' ')[0][-1]
    _coord = c.split(' ')[2][:-1].split(',')
    _size = c.split(' ')[3].split('x')
    return _id, _coord, _size


def checkOverlap(c1, c2):
    c1Id, c1Coord, c1Size = splitClaim(c1)
    c2Id, c2Coord, c2Size = splitClaim(c2)

    leftX = c1Coord[0]
    rightX = c1Coord[0] + c1Size[0]

    topY = c1Coord[1]
    bottomY = c1Coord[1] + c1Size[1]

    '''if  + c1Size[0] > c2Coord[0] + c2Size[0] or c1Coord[1] + c1Size[1] > c2Coord[1] + c2Size[1]:
        return True'''


for i in range(len(claims)-1):
    for j in range(i, len(claims)):
        if (checkOverlap(claims[i], claims[j])):
            print('Claims overlap')
