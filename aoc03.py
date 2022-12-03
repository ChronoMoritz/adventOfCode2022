import math

def a():
    file1 = open('./aoc03data.txt', 'r')
    Lines = file1.readlines()
    score = 0
    for line in Lines:
        amount = len(line)
        halfway = math.floor(amount/2)
        chars = []
        print(line, amount, halfway)
        for i in range(0, halfway):
            chars.append(line[i])
        for j in range(halfway, amount):
            if line[j] in chars:
                tmp = line[j]
                if tmp.isupper():
                    score += 26
                    tmp = tmp.lower()
                score += (ord(tmp) - 96)
                print(tmp, "ADD: ", (ord(tmp) - 96))
                break
        print(score)

def b():
    file1 = open('./aoc03data.txt', 'r')
    Lines = file1.readlines()
    score = 0
    index = 0
    for line in Lines:
        if index % 3 == 0:
            first = []
            second = []

            for char in Lines[index]:
                if char != '\n':
                    first.append(char)

            for char in Lines[index + 1]:
                if char != '\n' and char in first:
                    second.append(char)

            for char in Lines[index + 2]:
                if char != '\n' and char in second:
                    tmp = char
                    if tmp.isupper():
                        score += 26
                        tmp = tmp.lower()
                    score += (ord(tmp) - 96)
                    print(tmp, "ADD: ", (ord(tmp) - 96))
                    break
            print(score)
        index += 1

b()