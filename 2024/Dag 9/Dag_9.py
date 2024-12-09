def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    for i, line in enumerate(lines):
        line = line.strip('\n')
        for j, letter in enumerate(line):
            pass

def func2(line):
    line = line.strip('\n')
    string = []
    for i, p in enumerate(line):
        if i%2 == 0:
            # for _ in range(int(p)):
            string.append([int(i/2), int(p)])
        else:
            string.append(['.', int(p)])
    return string

def func(line):
    line = line.strip('\n')
    string = []
    for i, p in enumerate(line):
        if i%2 == 0:
            for j in range(int(p)):
                string.append(int(i/2))
        else:
            for _ in range(int(p)):
                string.append('.')
    return string

def sort(string):
    bp = 0
    ep = len(string)-1
    checksum = 0
    while bp < ep +1:
        v = string[bp]
        while v == '.':
            v = string[ep]
            ep -= 1
        # if abs(ep-bp) < 10:
        #     print('here')
        # if ep + 1 > bp:
        checksum += int(v)*bp
        bp += 1
    return checksum

def calcCheckSum(string: list):
    checkSum = 0
    offset = 0
    for i, v in enumerate(string):
        for _ in range(v[1]):
            if v[0] != '.':
                m = i+offset
                checkSum += m*v[0]
                # print(checkSum, m*v[0], m, v[0])
            offset += 1
        offset -= 1
    return checkSum


def sort2(string: list):
    ep = len(string)-1
    v: list
    while ep > 0:
        v = string[ep]
        if v[0] == '.':
            ep -= 1
            continue
        key, value = v
        if value == 0:
            ep -= 1
            continue

        for i, v2 in enumerate(string):
            if i > ep - 1:
                break
            if v2[0] == '.' and value < v2[1] + 1:
                string.pop(ep)
                string.insert(ep, ['.', value])
                string.pop(i)
                string.insert(i, v)
                rl = v2[1] -value
                if rl:
                    nl = ['.', rl]
                    string.insert(i+1, nl.copy())
                break
        ep -= 1                   

    return string

def buildString(string: list) -> str:
    ns = ''
    for s, r in string:
        for _ in range(r):
            ns += str(s)
    return ns


def part1():
    lines = readFile()
    # print(len(lines))
    r = func(lines[0])
    r = sort(r)
    print(r)

def part2():
    lines = readFile()
    r = func2(lines[0])
    print(buildString(r))
    r = sort2(r)
    print(buildString(r))
    r = calcCheckSum(r)
    print(r)

# part1()
part2()