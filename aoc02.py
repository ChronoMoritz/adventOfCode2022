
def a():
    file1 = open('./aoc02data.txt', 'r')
    Lines = file1.readlines()
    print(Lines)
    score = 0
    for line in Lines:
        if line[-1] == "\n":
            line = line[0:-1]
        if line == "A X": #Draw
            score += 4
        elif line == "A Y":  # WIN Paper
            score += 8
        elif line == "A Z": # LOOSE Scissor
            score += 3
        elif line == "B X": # Loose Rock
            score += 1
        elif line == "B Y": #Draw
            score += 5
        elif line == "B Z": # Win Scissor
            score += 9
        elif line == "C X": # Win Rock
            score += 7
        elif line == "C Y": # Loose Paper
            score += 2
        elif line == "C Z":
            score += 6      # DRAW
    print(score)

def b():
    file1 = open('./aoc02data.txt', 'r')
    Lines = file1.readlines()
    print(Lines)
    score = 0
    for line in Lines:
        if line[-1] == "\n":
            line = line[0:-1]
        if line == "A X":  # LOOSE Scissor
            score += 3
        elif line == "A Y":  # Draw
            score += 4
        elif line == "A Z":  # WIN Paper
            score += 8
        elif line == "B X":  # Loose Rock
            score += 1
        elif line == "B Y":  # Draw
            score += 5
        elif line == "B Z":  # Win Scissor
            score += 9
        elif line == "C X":  # Loose Paper
            score += 2
        elif line == "C Y":  # Draw
            score += 6
        elif line == "C Z":
            score += 7       # Win Rock
    print(score)





b()