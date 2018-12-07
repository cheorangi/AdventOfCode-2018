#read puzzle input from file
with open('day1p2-curtis-input.txt') as inFile:
    frequencies = [int(i) for i in inFile.read().splitlines()]

#use this puzzle to run your test cases
#puzzle = ['-6', '+3', '+8', '+5', '-6']

currFreq = 0

seen = set()

seen.add(currFreq)

cont = True
index = 0

while cont:
    if index > len(frequencies)-1:
        index = 0

    currFreq += frequencies[index]

    if currFreq in seen:
        print(currFreq)
        break

    seen.add(currFreq)

    index += 1