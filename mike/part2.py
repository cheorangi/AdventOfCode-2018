with open('input.txt') as f:
     input = f.read().strip().splitlines()
#print(read_data)
#input = open("input.txt").readlines()

for line in input:
    for letter in input:
        diffs = 0
        for index, char in enumerate(line):
            #print(idx,ch)
            if char != letter[index]:
                diffs += 1
        if diffs == 1:
            #ans is equal to each character in the line if it's the same as the letter in the other matching line
            ans = [char for index, char in enumerate(line) if letter[index] == char]
            print("Part Two:", ''.join(ans))