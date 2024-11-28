def loadExample():
    with open('ex_input.txt', 'r') as f:
        return f.readlines()

def loadInput(ind=0):
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        if ind:
            return lines[:ind]
        else:
            return lines
    
def findNums(line):
    nums = {}
    s = ''
    indices = set()
    for j, i in enumerate(line):
        if i in '0123456789':
            s += i
            indices.add(max(0, j-1))
            indices.add(j)
            indices.add(min(len(line)-1, j+1))
        elif s:
            nums[int(s)] = indices.copy()
            s = ''
            indices = set()
    if s:
        nums[int(s)] = indices.copy()  
    return nums

def findSymbols(line):
    symbs = {}
    for j, i in enumerate(line):
        if i in '.0123456789':
            continue
        elif i in symbs:
            symbs[i].append(j)
        else:
            symbs[i] = [j]
    return symbs

def parseLine(line: str):
    if '\n' in line:
        line = line[:-1]
    return {'numbs': findNums(line), 'symbs': findSymbols(line)}
                
def checkNum(indices: set, rows):
    for pl in rows:
        for ind in indices:
            for symb, symbIndices in pl['symbs'].items():
                if ind in symbIndices:
                    return True
    return False

def calcPartNSum(allParsedLines):
    s = 0
    for ind, pl in enumerate(allParsedLines):
        # print('\n', str(ind) + ': ', end='')
        for num, indices in pl['numbs'].items():
            rows = allParsedLines[max(0, ind-1):min(len(allParsedLines), ind+2)]
            if checkNum(indices, rows):
                # print(num, end='')
                s += num
    return s

def createActiveMatrix(lines):
    active = {}
    for lineInd in range(1, len(lines)):
        line = lines[lineInd].strip('\n')
        for ind, i in enumerate(line):
            if i in ".0123456789":
                pass
            else:
                for j in range(lineInd-1, lineInd+2):
                    if j in active:
                        active[j].append(max(0, ind-1))
                        active[j].append(ind)
                        active[j].append(min(ind+1, len(lines)))
                    else:
                        active[j] = [max(0, ind-1), ind, min(ind+1, len(line))].copy()

    retActive = {}
    for i, j in active.items():
        retActive[i] = set(j)
        # print(i, retActive[i])
    return retActive

def findPartNr(lines, activeMatrix):
    partNr = {}
    for i, line in enumerate(lines):
        line = line.strip('\n')
        number = ''
        addNumber = False
        for j, s in enumerate(line):
            if s in '0123456789':
                number += s
                if j in activeMatrix[i]:
                    addNumber=True
            elif number and addNumber:
                if i in partNr:
                    partNr[i].append(int(number))
                else:
                    partNr[i] = [int(number)]
                addNumber = False
                number = ''
        if number and addNumber:
            if i in partNr:
                partNr[i].append(int(number))
            else:
                partNr[i] = [int(number)]
    return partNr


def part1():
    lines = loadExample()
    # parsedLines = []
    # for i, line in enumerate(lines):
    #     parsedLine = parseLine(line)
    #     print(parsedLine)
    #     parsedLines.append(parsedLine)
    
    # print(calcPartNSum(parsedLines))

    am = createActiveMatrix(lines)
    pn = findPartNr(lines, am)
    s = 0
    for i in pn.values():
        s += sum(i)
    print(s)
part1()
