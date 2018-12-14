#import timeit
import time

start = time.clock()
#supply the input as a txt file for this to work
#writes each line into a list where each line is an index in the list
#with open('day1p1-curtis-input.txt') as inFile:
    #frequencies = [int(i) for i in inFile.read().splitlines()]
print(sum([int(i) for i in open('day1p1-curtis-input.txt').read().splitlines()]))
end = time.clock()

print(end-start)
#convert all strings to ints in the list of frequencies
#frequencies = [int(i) for i in puzzle]

#print frequencies for debugging purposes
#print(frequencies[0])

#output the puzzle solution 
# utilizing the sum function to calculate the sum of postive and negative values.
#print(sum(frequencies))
