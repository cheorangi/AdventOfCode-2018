#read puzzle input from file
with open('day1p2-curtis-input.txt') as inFile:
    frequencies = [int(i) for i in inFile.read().splitlines()]

#use this puzzle to run your test cases
#puzzle = ['-6', '+3', '+8', '+5', '-6']

currFreq = 0

seen = set()

seen.add(currFreq)

cont = True

while cont:
    for i in frequencies:
        currFreq += i

        if currFreq in seen:
            print(currFreq)
            cont = False
            break

        seen.add(currFreq)
