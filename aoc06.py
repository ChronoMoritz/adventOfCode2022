def a():
    file1 = open('./aoc06data.txt', 'r')
    Lines = file1.readlines()
    score = 0
    overlapscore = 0
    state = [[]]
    solution = ""
    for line in Lines:
        str = "a" + line[0:3]
        i = 4
        for char in line[3:]:
            str = str[1:]
            str = str+char
            if str.count(str[0]) == 1 and str.count(str[1]) == 1 and str.count(str[2]) == 1 and str.count(str[3]) == 1:
                print(i)
                break
            i += 1
def b():
    file1 = open('./aoc06data.txt', 'r')
    Lines = file1.readlines()
    score = 0
    overlapscore = 0
    state = [[]]
    solution = ""
    for line in Lines:
        str = "a" + line[0:13]
        i = 14
        for char in line[13:]:
            str = str[1:]
            str = str+char
            finished = 1
            for j in range(len(str)):
                if str.count(str[j]) !=1:
                    finished = 0
                    break
            if(finished == 1):
                print(i)
                break

            i += 1
b()