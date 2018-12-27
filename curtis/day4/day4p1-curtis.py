from collections import Counter
#chars to remove from string
charsToStrip = '[]'

#setting up my file for day 4 if i every get there lol
with open('day4p1-curtis-input.txt') as infile:
    data = [''.join(c for c in x if c not in charsToStrip) for x in infile.read().splitlines()]

#sort data by time inlcuding hour and minute
data.sort(key = lambda x : x.split(' ')[0] + ' ' + x.split(' ')[1])

#create dictionary to store gaurds times asleep. Format with be like this - {id: timeasleep}
guards = {}

#initialize start and end to avoid unset error in loop below
start = 0
end = 0

#create dictionary with guard id as the key and nest dictionnary with the dates and a list containing the minutes sleep on that date.
for i in range(len(data)):
    if 'Guard' in data[i]:
        date = data[i].split(' ')[0]
        ID = data[i].split(' ')[3][1:]
        if ID not in guards.keys():
            guards[ID] = {date:[]}
        else:
            guards[ID][date] = []
        start = 0
        end = 0

    if 'asleep' in data[i]:
        start = data[i].split(' ')[1].split(':')[1]

    if 'wakes' in data[i]:
        end = data[i].split(' ')[1].split(':')[1]

    if start != 0 and end != 0:
        if ID in guards.keys():
            if date in guards[ID].keys():
                for i in range(int(start), int(end)):
                    guards[ID][date].append(i)
        else:
            guards[ID][date] = [i for i in range(int(start), int(end))]#timeAsleep
        start = 0
        end = 0
        

d = max(guards.keys(), key=(lambda key: guards[key]))

g = ''
m = 0
#get the guard ID
for i in guards.keys():
    #get the dates for that guard and check the length of the list containing the minutes they were asleep.
    for j in guards[i].keys():
        print(guards[i][j])
        if len(guards[i][j]) >= m:
            g = i
            m = len(guards[i][j])

print('guard: {}, minutes asleep: {}'.format(g, m))

minuteCounts = {}

for d in guards[g]:
    for i in guards[g][d]:
        if i not in  minuteCounts:
            minuteCounts[i] = 1
        else:
            minuteCounts[i] += 1

k = max(minuteCounts.keys(), key=(lambda key: minuteCounts[key]))
print('Minute Most Asleep: {}'.format(k))
#print(minuteCounts[k])
answer = int(g) * int(k)
print('Answers = {}'.format(str(answer)))


    

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

