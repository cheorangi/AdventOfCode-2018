with open('day1p2-input.txt') as inFile:
    puzzle = inFile.read().splitlines()

#convert all strings to ints in the list of frequencies
frequencies = [int(i) for i in puzzle]

_sum = 0


for i in range(len(frequencies)):
    