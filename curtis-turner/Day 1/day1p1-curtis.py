#supply the input as a txt file for this to work
#writes each line into a list where each line is an index in the list
with open('day1p1-input.txt') as inFile:
    puzzle = inFile.read().splitlines()

#convert all strings to ints in the list of frequencies
frequencies = [int(i) for i in puzzle]

#print frequencies for debugging purposes
# print(frequencies)

#output the puzzle solution 
# utilizing the sum function to calculate the sum of postive and negative values.
print(sum(frequencies))
