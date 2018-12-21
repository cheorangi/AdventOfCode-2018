from itertools import takewhile
#chars to remove from string
charsToStrip = '[]'

#setting up my file for day 4 if i every get there lol
with open('day4p1-curtis-input.txt') as infile:
    data = [''.join(c for c in x if c not in charsToStrip) for x in infile.read().splitlines()]

#sort data by time inlcuding hour and minute
data.sort(key = lambda x : x.split(' ')[0] + ' ' + x.split(' ')[1])

#create dictionary to store gaurds times asleep. Format with be like this - {id: timeasleep}
guards = dict()

def countTimeAsleep(id, d):
    for i in range(len(d)):
        if id in d[i]:
            print(d[i])

#create gaurd id in dictionary with initial value of zero
for i in range(len(data)):
    startMinute = 0
    endMinute = 0
    if 'Guard' in data[i]:
        ID = data[i].split(' ')[3][1:]
        if guards.get(ID) == None:
            guards[ID] = 0

        onDuty = True
        j = i + 1
        while onDuty:
            if 'asleep' in data[j]:
                startMinute = i.split(' ')[1].split(':')[1]

            if 'wakes' in data[j]:
                endMinute = i.split(' ')[1].split(':')[1]

            if startMinute != 0 and endMinute != 0:
                timeAsleep = endMinute - startMinute
                guards[ID] += timeAsleep

print(guards['3167'])
        
'''
if any(gaurd for gaurd in gaurds if gaurd['id'] == gaurdID):
            gaurd = next(gaurd for gaurd in gaurds if gaurd['id'] == gaurdID)
        else:
            gaurd = {'date': i.split(' ')[0] + ' ' + i.split(' ')[1], 'id': gaurdID, 'asleep': 0}
            gaurds.append(gaurd)

print(newdata)

gaurds = [{'date': '11-01', 'id': '#123' , 'minutes': 0}]

def countOfMinutesAwake(id, data):
    totalMinutesAwake = 0
    for i in data:
        if id in i:
            print('Id is in this line of the data...')
    
    return totalMinutesAwake


for i in newdata:
    print(i)
    if 'Gaurd' in i:
        gaurdNum = i.split(' ')[2]
        print(gaurdNum)
        if gaurdNum not in gaurds:
            gaurds[gaurdNum] = 0
        else:
            gaurds[gaurdNum] = countOfMinutesAwake(gaurdNum, newdata)

with open('check-data.txt', 'w') as outfile:
    for i in newdata:
        outfile.write(i + '\n')

Notes in the Comment
addtime = map(lambda l : l[0].split(' ')[0] + ' ' + l[0].split(' ')[1], data)
print(list(addtime))
print(data[0])


newdata =[]
for i in range(len(data)):
    temp = ''
    string = data[i]
    timestamp = string.split(' ')[0] + ' ' + string.split(' ')[1]
    timestamp = timestamp[1:-1]
    timestap = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    temp += timestamp + ' ' + data[i]
    newdata.append(temp)

#print(newdata[0])

with open('check-data-3.txt', 'w') as outfile:
    for i in data:
        outfile.write(i + '\n')
'''

