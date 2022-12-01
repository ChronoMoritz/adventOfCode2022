file1 = open('./aoc01data.txt', 'r')
Lines = file1.readlines()
maxElve = 0
max2Elve = 0
max3Elve = 0
tmp = 0
for line in Lines:
    if line != "\n":
        tmp = tmp + int(line)
    else:
        if tmp > max3Elve:
            if(tmp > max2Elve):
                if(tmp > maxElve):
                    max3Elve = max2Elve
                    max2Elve = maxElve
                    maxElve = tmp
                else:
                    max3Elve = max2Elve
                    max2Elve = tmp
            else:
                print("here with:", tmp)
                max3Elve = tmp
        tmp = 0

print(maxElve, max2Elve, max3Elve)
print("CombinedElves: ", maxElve + max2Elve + max3Elve)
print("maximum Elve:", maxElve)