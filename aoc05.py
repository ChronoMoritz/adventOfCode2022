def a():
    file1 = open('./aoc05data.txt', 'r')
    Lines = file1.readlines()
    score = 0
    overlapscore = 0
    state = [[]]
    solution = ""
    for line in Lines:
        if "[" in line:
            length = len(line)
            print(line)
            i = 1
            j = 1
            while i < length:
                if len(state) <= j:
                    state.append([])
                if line[i] != " ":
                    tmp = state[j]
                    tmp.append(str(line[i]))
                    state[j] = tmp
                i = i + 4
                j = j+1
            
        elif line[0] == " ":
            print(line)

        elif line == "\n":
            for i in range(0, len(state)):
                state[i] = list(reversed(state[i]))

        else:
            x = line
            if line[-1] == "\n":
                x = line[0: -1]
            tmp = x.split(" ")
            print(tmp)
            for i in range(0, int(tmp[1])):
                obj = state[int(tmp[3])][-1]
                state[int(tmp[5])].append(obj)
                state[int(tmp[3])] = state[int(tmp[3])][:-1]
                print(obj)
    for x in state[1:]:
        solution = solution + x[-1]
    print(solution)

def b():
    file1 = open('./aoc05data.txt', 'r')
    Lines = file1.readlines()
    score = 0
    overlapscore = 0
    state = [[]]
    solution = ""
    for line in Lines:
        if "[" in line:
            length = len(line)
            print(line)
            i = 1
            j = 1
            while i < length:
                if len(state) <= j:
                    state.append([])
                if line[i] != " ":
                    tmp = state[j]
                    tmp.append(str(line[i]))
                    state[j] = tmp
                i = i + 4
                j = j+1
            
        elif line[0] == " ":
            print(line)

        elif line == "\n":
            for i in range(0, len(state)):
                state[i] = list(reversed(state[i]))

        else:
            x = line
            if line[-1] == "\n":
                x = line[0: -1]
            tmp = x.split(" ")
            print(tmp)
            for i in range(0, int(tmp[1])):
                j = int(tmp[1]) - i
                pos = 0 -j
                obj = state[int(tmp[3])][pos]
                state[int(tmp[5])].append(obj)
                print(obj)
            pos = 0 - int(tmp[1])
            state[int(tmp[3])] = state[int(tmp[3])][:pos]
    for x in state[1:]:
        solution = solution + x[-1]
    print(solution)            

b()