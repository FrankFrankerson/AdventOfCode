def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    allPatterns = []
    currPattern = []
    for i, line in enumerate(lines):
        line = line.strip('\n')
        if line == '':
            allPatterns.append(currPattern.copy())
            currPattern = []
        else:
            currPattern.append(line)
    allPatterns.append(currPattern.copy())
    return allPatterns
    
def checkPatternHorizontal(pattern: list, smudgeCounter = 0):
    row1Ptr = 0
    l = len(pattern)
    while row1Ptr < l-1:
        row1 = pattern[row1Ptr]
        row2 = pattern[row1Ptr + 1]
        difference = checkDifference(row1, row2, smudgeCounter)
        if len(difference) < smudgeCounter + 1:
            newSmudgeCounter = smudgeCounter
            r1Ptr = row1Ptr
            r2Ptr = row1Ptr + 1
            equal = True
            while r1Ptr > -1 and r2Ptr < l:
                r1 = pattern[r1Ptr]
                r2 = pattern[r2Ptr]
                rowDifference = checkDifference(r1, r2, newSmudgeCounter)
                if len(rowDifference) > newSmudgeCounter:
                    equal = False
                    break
                elif rowDifference:
                    newSmudgeCounter -= 1
                r1Ptr -= 1
                r2Ptr += 1
            if equal and newSmudgeCounter == 0:
                return row1Ptr
        row1Ptr += 1
        
    return -1

def checkVertical(pattern: list, smudgeCounter=0):
    np = []
    for i in range(len(pattern[0])):
        r = ''
        for j in pattern:
            r += j[i]
        np.append(r)
    return checkPatternHorizontal(np, smudgeCounter)

def checkDifference(row1, row2, maxDiff=0):
    diffScore = []
    for i, s in enumerate(row1):
        if s != row2[i]:
            diffScore.append(i)
            if len(diffScore) > maxDiff:
                return diffScore
    return diffScore

def part1():
    lines = readFile(1)
    patterns = parseLines(lines)

    total = 0
    for pattern in patterns:
        rH = checkPatternHorizontal(pattern)
        if rH > -1:
            total += (rH+1)*100
        else:
            rV = checkVertical(pattern)
            total += rV + 1
    print(total)

def part2():
    lines = readFile(1)
    patterns = parseLines(lines)

    total = 0
    for i, pattern in enumerate(patterns):
        rH = checkPatternHorizontal(pattern, smudgeCounter=1)
        if rH > -1:
            print(f'{i:3} Horizontal:', rH)
            total += (rH+1)*100
        else:
            rV = checkVertical(pattern, smudgeCounter=1)
            print(f'{i:3} Vertical:', rV)
            if rV < 0:
                print(pattern)
            total += rV + 1
    print(total)

# part1()
part2()