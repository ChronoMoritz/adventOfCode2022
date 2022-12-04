def a():
    file1 = open('./aoc04data.txt', 'r')
    Lines = file1.readlines()
    score = 0
    overlapscore = 0
    for line in Lines:
        parts = line.split(",")
        sectionsa = []
        sectionsb = []
        detailA = parts[0].split("-")
        detailB = parts[1].split("-")
        if detailB[1][-1] == "\n":
            detailB[1] = detailB[1][0:-1]
        for i in range(int(detailA[0]), int(detailA[1]) +1):
            sectionsa.append(i)

        for i in range(int(detailB[0]), int(detailB[1])+1):
            sectionsb.append(i)
        doubledA = 1
        doubledB = 1
        overlap = 0
        for char in sectionsa:
            if char not in sectionsb:
                doubledA = 0
            if char in sectionsb:
                overlap = 1

        for char in sectionsb:
            if char not in sectionsa:
                doubledB = 0

        if doubledA == 1 or doubledB == 1:
            score += 1
        if overlap == 1:
          overlapscore +=1
    print("SCORE: ", score)
    print("OVERLAP SCORE: ", overlapscore)
a()