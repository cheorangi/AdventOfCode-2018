import datetime
import re

#setting up my file for day 4 if i every get there lol
with open('day4p1-curtis-input.txt') as infile:
    data = infile.read().splitlines()

newdata =[]
for i in range(len(data)):
    temp = []
    string = data[i]
    timestamp = string.split(' ')[0] + ' ' + string.split(' ')[1]
    timestamp = timestamp[1:-1]
    timestap = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    temp.append(timestamp)
    temp +=  ' ' + data[i]
    newdata.append(temp)

print(newdata[0])

'''
Notes in the Comment
addtime = map(lambda l : l[0].split(' ')[0] + ' ' + l[0].split(' ')[1], data)
print(list(addtime))
print(data[0])
'''

