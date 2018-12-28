#chars to remove from string
charsToStrip = '[]'

#parse file and format date properly
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
        
guardID = None
m = 0
#get the guard ID
for i in guards.keys():
    #get the dates for that guard and check the length of the list containing the minutes they were asleep.
    for j in guards[i].keys():
        #find guard with the most minutes asleep
        if len(guards[i][j]) >= m:
            guardID = i
            m = len(guards[i][j])


minuteCounts = {}

for d in guards[guardID]:
    for i in guards[guardID][d]:
        if i not in  minuteCounts:
            minuteCounts[i] = 1
        else:
            minuteCounts[i] += 1

minute = max(minuteCounts.keys(), key=(lambda key: minuteCounts[key]))

print('Answers Part 1: {}'.format(str(int(guardID) * int(minute))))

#part 2
newGuards = {}
for g in guards:
    for d in guards[g]:
        for m in guards[g][d]:
            if (g, m) not in newGuards:
                newGuards[(g, m)] = 1
            else:
                newGuards[(g, m)] += 1

guard = None
for k, v in newGuards.items():
    if guard is None or v > newGuards[guard]:
        guard = k

print('Answer Part 2: {}'.format(int(guard[0]) * int(guard[1])))