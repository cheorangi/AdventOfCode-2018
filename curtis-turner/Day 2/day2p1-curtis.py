from collections import Counter

with open('day2p1-curtis-input.txt') as infile:
    ids = infile.read().splitlines()

#ids = ['abcdef',  'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

twos = 0 
threes = 0

#count number of strings with two matching chars
for id in ids:
    counter = Counter(id)
    for c in id:
        count = counter[c]
        if count == 2:
            twos += 1
            break
            
#count the number of strings with three matching chars
for id in ids:
    counter = Counter(id)
    for c in id:
        count = counter[c]
        if count == 3:
            threes += 1
            break

print(str(twos))
print(str(threes))

checksum = twos * threes

print(checksum)