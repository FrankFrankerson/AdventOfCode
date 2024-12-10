def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    data = []
    for i, line in enumerate(lines):
        line = line.strip('\n')
        data.append(line)
    return data

def transpose(lines):
    np = []
    for i in range(len(lines[0])):
        r = ''
        for line in lines:
            r += line[i]
        np.append(r)
    return np

def findPosition(line, sym):
    indices = []
    for i, s in enumerate(line):
        if s == sym:
            indices.append(i)
    return indices

def tiltLeft(lines):
    lines = transpose(lines)
    data = []
    for line in lines:
        l = len(line)
        rocksIndices = findPosition(line, '#')
        parts = line.split('.')
        nl = ''
        for part in parts:
            if part == '':
                continue
            for s in part:
                if s == 'O':
                    nl += 'O'
                elif s == '#':
                    p = rocksIndices.pop(0)
                    while p < len(nl):
                        p = rocksIndices.pop(0)
                    dotN = p - len(nl)
                    nl += '.'*dotN + '#'
        dotN = l - len(nl)
        nl += '.'*dotN
        data.append(nl)
    return transpose(data)

def calcDistance(data):
    dist = 0
    for line in data:
        rockIndices = findPosition(line, 'O')
        l = len(line)
        for i in rockIndices:
            dist += l-i
    return dist

def printGrid(data, rotation=0):
    # data = transpose(data)
    for i in range(rotation):
        data = rotateClockWise(data)
    for line in data:
        print(line)

def rotateClockWise(data):
    data = transpose(data)
    new = []
    for line in data:
        nl = ''
        for i in reversed(line):
            nl += i
        new.append(nl)
    return new

def part1():
    lines = readFile(1)
    data = transpose(parseLines(lines))
    data = tiltLeft(data)
    dist = calcDistance(data)
    print(dist)


def part2():
    lines = readFile()
    data = parseLines(lines)
    printGrid(data)
    # for i in range(1):
    #     data = tiltLeft(data)
    #     data = rotateCounterClockWise(data)
    print('--------TILTED-----------')
    data = tiltLeft(data)
    printGrid(data)
    for i in range(3+4*(1000000000-1)):
        data = rotateClockWise(data)
        data = tiltLeft(data) 
        if i%1000 == 0:
            print(f'--------ROTATED {i}----------')
        # printGrid(data, 4-1-i%4)       
   
    dist = calcDistance(data)
    print(dist)

# part1()
part2()