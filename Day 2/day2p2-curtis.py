#import time to test how long it takes the algorithm to run.
import time

#test data from the example
#ids = ['abcde', 'fghij', 'klmno', 'pqrst',  'fguij' ,'axcye', 'wvxyz']

#start timeer
start = time.perf_counter()

#open file with puzzle input
with open('day2p2-curtis-input.txt') as infile:
    ids = infile.read().splitlines()

#iterate all strings from the input
for i in range(len(ids)-1):
    for j in range(len(ids)-1):
        #make sure strings are not equal
        if ids[i] != ids[j]:
            #get the count of chars in the string that are not equal
            count = sum(1 for a, b in zip(ids[i], ids[j]) if a != b)
            if count == 1:
                #set temp vars for ease of use below
                s1 = ids[i]
                s2 = ids[j]
                output = [i for i in range(len(s1)) if s1[i] != s2[i]]
                #create the answer string will all the chars in the correct order removing the char that doest match
                answer = ''
                for c1, c2 in zip(s1, s2):
                    if c1 == c2:
                        answer += c1
                print(answer)
                
end = time.perf_counter()

#print time it took to run code
print(end-start)