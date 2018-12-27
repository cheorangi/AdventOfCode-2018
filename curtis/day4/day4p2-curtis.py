#chars to remove from string
charsToStrip = '[]'

#setting up my file for day 4 if i every get there lol
with open('day4p1-curtis-input.txt') as infile:
    data = [''.join(c for c in x if c not in charsToStrip) for x in infile.read().splitlines()]

#sort data by time inlcuding hour and minute
data.sort(key = lambda x : x.split(' ')[0] + ' ' + x.split(' ')[1])

#create dictionary to store gaurds times asleep. Format with be like this - {id: timeasleep}