def loadExample():
    with open('ex_input.txt', 'r') as f:
        return f.readlines()

def loadInput():
    with open('input.txt', 'r') as f:
        return f.readlines()
    
def findNums(line):
    nums = []
    s = ''
    indices = set()
    for j, i in enumerate(line):
        if i in '0123456789':
            s += i
            m = max(0, j-1)
            indices.add(m)
            indices.add(j)
            indices.add(min(len(line), j+1))
        elif s:
            d = {'n': int(s), 'i': indices.copy()}
            nums.append(d)
            s = ''
            indices = set()
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
    line = line.strip('\n')
    return {'numbs': findNums(line), 'symbs': findSymbols(line)}
              

def checkIfPartN(parsedLine, checkLines, allLines):
    for num in parsedLine['numbs']:
        for line in checkLines:
            for ind in num['i']:
                for sym in allLines[line]['p']['symbs'].values():
                    if ind in sym:
                        return True
    


def part1():
    lines = loadExample() 
    parsedLines = []
    for i, line in enumerate(lines):
        checkLines = set(max(0, i-1), i, min(len(lines) + 1, i+1))
        parsedLine = parseLine(line)
        parsedLines.append({'c': checkLines, 'p': parsedLine})
    
    for l in parsedLines:
        if l['p']['numbs']:
            checkIfPartN(l['p'], l['c'], parsedLines)



part1()
