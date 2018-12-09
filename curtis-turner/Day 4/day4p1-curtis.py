import datetime
import re

class Guard():
    def __init__(self, id, minutes):
        self.id = id
        self.minutes = minutes

#setting up my file for day 4 if i every get there lol
with open('day4p1-curtis-input.txt') as infile:
    data = infile.read().splitlines()

newdata =[]
for i in range(len(data)):
    temp = ''
    string = data[i]
    timestamp = string.split(' ')[0] + ' ' + string.split(' ')[1]
    timestamp = timestamp[1:-1]
    timestap = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    temp += timestamp + ' ' + data[i]
    newdata.append(temp)

print(newdata[0])

newdata.sort(key = lambda x : x.split(' ')[0])

print(newdata[0])

gaurds = []

#track the guard IDs and then track the minutes that they are asleep
#if gaurdID array of gaurds 
for i in newdata:
    if 'Gaurd' in i.split(' '):
        gaurdNum = i.split(' ')[2]
        if gaurdNum not in gaurds:
            gaurds[gaurdNum] = 0
        else:
            gaurds[gaurdNum] += 

'''with open('check-data.txt', 'w') as outfile:
    for i in newdata:
        outfile.write(i + '\n')

Notes in the Comment
addtime = map(lambda l : l[0].split(' ')[0] + ' ' + l[0].split(' ')[1], data)
print(list(addtime))
print(data[0])
'''

