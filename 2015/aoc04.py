import hashlib


def fiveZeroes():
    file1 = open('./aoc04data.txt', 'r')
    lines = file1.readlines()
    i = 1
    finished = 0
    for line in lines:
        while finished == 0:
            key = line + str(i)
            hash = hashlib.md5(key.encode())
            tmp = str(hash.hexdigest())
            if tmp[0:5] == "00000":
                finished = 1
                print(tmp, i, key)
            i += 1

def sixZeroes():
    file1 = open('./aoc04data.txt', 'r')
    lines = file1.readlines()
    i = 1
    finished = 0
    for line in lines:
        while finished == 0:
            key = line + str(i)
            hash = hashlib.md5(key.encode())
            tmp = str(hash.hexdigest())
            if tmp[0:6] == "000000":
                finished = 1
                print(tmp, i, key)
            i += 1

def test():
    tmp = "abcdef609043"
    hash = hashlib.md5(tmp.encode())
    print(hash.hexdigest())

sixZeroes()