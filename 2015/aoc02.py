file1 = open('./aoc02data.txt', 'r')
Lines = file1.readlines()
total = 0
ribbon = 0
for line in Lines:
    if line[-1] == "\n":
        line = line[:-1]
    tmp = line.split("x")
    l = int(tmp[0])
    w = int(tmp[1])
    h = int(tmp[2])
    print(l*w, h*w, h*l)
    ribbon += (l*w*h + 2*l + 2*w + 2*h - 2*max(l, w, h))
    total += (2*l*w + 2*w*h + 2*h*l + min(l*w , w*h, h*l))
print("Total: ", total)
print("Ribbon: ", ribbon)


