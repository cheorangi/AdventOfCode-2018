#supply the input as a txt file for this to work.
with open('day1p1-input.txt') as inFile:
    puzzle = inFile.read().splitlines()

frequencies = [int(i) for i in puzzle]
print(frequencies)
print(sum(frequencies))
