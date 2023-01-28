file1 = open('./aoc01data.txt', 'r')
Lines = file1.readlines()
floor = 0
pos = 0
first = 1
for line in Lines:
    for char in line:
        pos += 1
        if char == "(":
            floor += 1
        if char == ")":
            floor -= 1
            if floor == -1 and first == 1:
                print(pos)
                first = 0

print(floor)
