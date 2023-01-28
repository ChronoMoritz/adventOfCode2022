def aloneSanta():
    file1 = open('./aoc03data.txt', 'r')
    Lines = file1.readlines()
    x = 0
    y = 0
    visits = [[0, 0]]
    doubles = 0
    multiple = 0
    dvisits = []
    overall = 1
    for line in Lines:
        for char in line:
            if char != "\n":
                    if char == "<":
                        x = x - 1
                    if char == ">":
                        x = x + 1
                    if char == "^":
                        y = y + 1
                    if char == "v":
                        y = y - 1
                    tmp = [x, y]
                    if tmp in visits:
                        multiple += 1
                        if tmp not in dvisits:
                            doubles += 1
                            dvisits.append(tmp)

                    overall += 1
                    visits.append(tmp)
    print("ALONE SANTA")
    print("Number of visits:", overall)
    print("Number of visist that were allready visited: ", multiple)
    print("Number of houses with  multiple presents: ", doubles)
    print("Number of houses with at least one present: ", overall - multiple)

def roboSanta():
    file1 = open('./aoc03data.txt', 'r')
    Lines = file1.readlines()
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    visits = [[0, 0]]
    doubles = 0
    multiple = 0
    dvisits = []
    overall = 1
    for line in Lines:
        for char in line:
            if char != "\n":
                if (overall % 2) == 0:
                    if char == "<":
                        x = x - 1
                    elif char == ">":
                        x = x + 1
                    elif char == "^":
                        y = y + 1
                    elif char == "v":
                        y = y - 1
                    tmp = [x, y]
                    if tmp in visits:
                        multiple += 1
                        if tmp not in dvisits:
                            doubles += 1
                            dvisits.append(tmp)

                    overall += 1
                    visits.append(tmp)

                elif (overall % 2) == 1:
                    if char == "<":
                        x1 = x1 - 1
                    elif char == ">":
                        x1 = x1 + 1
                    elif char == "^":
                        y1 = y1 + 1
                    elif char == "v":
                        y1 = y1 - 1
                    tmp = [x1, y1]
                    if tmp in visits:
                        multiple += 1
                        if tmp not in dvisits:
                            doubles += 1
                            dvisits.append(tmp)

                    overall += 1
                    visits.append(tmp)

    print("ROBO SANTA")
    print("Number of visits:", overall)
    print("Number of visist that were allready visited: ", multiple)
    print("Number of houses with  multiple presents: ", doubles)
    print("Number of houses with at least one present: ", overall - multiple)

aloneSanta()
print("")
roboSanta()
