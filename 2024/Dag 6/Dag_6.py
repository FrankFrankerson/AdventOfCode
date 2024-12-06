def readFile(inp=0):
    if inp:
        fileName = 'input.txt'
    else:
        fileName ='ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()
    
import copy

def findStart(lines):
    txt = []
    line: str
    for i, line in enumerate(lines):
        line = line.strip('\n')
        txt.append(line)
        if "^" in line:
            start = (i , line.find('^'))
            dir = 0
        elif "<" in line:
            start = (i , line.find('<'))
            dir = 3
        elif ">" in line:
            start = (i , line.find('>'))
            dir = 1
        elif "v" in line:
            start = (i , line.find('v'))
            dir = 2
    return txt, start, dir

def checkPos(np, lines, OL = (-1,-1)):
    i = np[0]
    j = np[1]
    if i < 0 or i > len(lines) - 1 or j < 0 or j > len(lines[0]) - 1:
        return True, True
    
    if lines[i][j] == '#':
        return False, False
    
    if i == OL[0] and j == OL[1]:
        return False, False

    return True, False

def checkOL(loc, lines):
    obs, outside = checkPos(loc, lines)
    if not obs or outside:
        return False
    return True


def step(loc, dir):
    if dir == 0:
        np = (loc[0] - 1, loc[1])
    elif dir == 1:
        np = (loc[0], loc[1] + 1)
    elif dir == 2:
        np = (loc[0]+1, loc[1])
    else:
        np = (loc[0], loc[1]-1)
    return np


def walk(start, dir, lines):
    pos = [start]
    loc = start
    end = False

    while not end:
        # print('---',loc, dir)
        np = step(loc, dir)
        t, e = checkPos(np, lines)
        if e:
            end = True
        elif t:
            loc = np
            if loc not in pos:
                pos.append(loc)
        else:
            dir += 1
            dir %= 4
    return pos

def walkLoop(currPos, dir, lines, OL):
    pos = {}
    for i in range(4):
        pos[i] = [].copy()
    pos[dir].append(currPos)

    loc = currPos
    end = False

    while not end:
        # print('---',len(pos))

        np = step(loc, dir)
        t, e = checkPos(np, lines, OL)
        if e:
            return False
        elif t:
            loc = np
            if loc not in pos[dir]:
                pos[dir].append(loc)
            else:
                return True
        else:
            dir += 1
            dir %= 4
    return False


def walk2(start, dir, lines, m):
    # pos = [[start, dir]]
    pos = {}
    for i in range(4):
        pos[i] = [].copy()
    pos[dir].append(start)

    startDir = dir
    loc = start
    end = False
    checkedLocs = []
    OLLocs = []
    posCounter = 0
    while not end:
        # print(loc, dir)
        np = step(loc, dir)
        t, e = checkPos(np, lines)
        if e:
            end = True
        elif t:
            loc = np
            if loc not in pos[dir]:
                posCounter += 1
                pos[dir].append(loc)
                # print('CheckLoop', f'{100*posCounter/m:.2}%', len(checkedLocs), len(OLLocs))
                for i in range(4):
                    olLoc = step(loc, (dir+i)%4)
                    # olLoc = loc
                    OLok = checkOL(olLoc, lines)                    
                    if olLoc != start and OLok:
                        if olLoc not in checkedLocs: 
                            checkedLocs.append(olLoc)
                            if walkLoop(start, startDir, lines, olLoc):
                                OLLocs.append(olLoc)
        else:
            dir += 1
            dir %= 4
    return pos, OLLocs

def part1():
    lines = readFile(1)
    lines, start, dir = findStart(lines)
    pos = walk(start, dir, lines)
    print(len(pos))
    return len(pos)

def part2(m):
    lines = readFile(1)
    lines, start, dir = findStart(lines)
    pos, c = walk2(start, dir, lines, m)
    print('pos', len(pos),'places', len(c))


m = part1()
part2(m)