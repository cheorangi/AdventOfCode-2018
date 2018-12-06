#read puzzle input from file
with open('day1p2-curtis-input.txt') as inFile:
    puzzle = inFile.read().splitlines()

#use this puzzle to run your test cases
#puzzle = ['-6', '+3', '+8', '+5', '-6']

#convert all strings to ints in the list of frequencies
frequencies = [int(i) for i in puzzle]

#print(frequencies)

currFreq = 0

seen = set()

cont = True
index = 0

seen.add(currFreq)

while (cont):
    if index > (len(frequencies)-1):
        index = 0
    #print('current value >> ' + str(frequencies[index]))
    #print('current frequency >> ' + str(currFreq))
    
    currFreq = currFreq + frequencies[index]

    #print(seen)
    #print('current sum >> ' + str(_sum))
    

    if currFreq in seen:
        print(currFreq)
        break

    seen.add(currFreq)

    index += 1