input = open("input.txt").readlines()

def count_letter(mystring):
    d = {}
    twos = False
    threes = False
# count occurances of character
    for w in mystring: 
        d[w] = mystring.count(w)
# print the result
    for k in d:
        if d[k] == 2:
            #print (k + ': ' + str(d[k]))
            twos = True
        elif d[k] == 3:
            #print (k + ': ' + str(d[k]))
            threes = True
        else:
            continue
    return mystring.strip(), twos, threes

num1 = 0
num2 = 0
for box in input:
    box = count_letter(box)
    if box[1] == True:
        num1 += 1
    if box[2] == True:
        num2 += 1
checksum = num1 * num2
print(checksum)