import time

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    for i, line in enumerate(lines):
        line = line.strip('\n')
        for j, letter in enumerate(line):
            pass
    
class Grid:
    def __init__(self, lines, name='mainGrid', val='.') -> None:
        txt = []
        for line in lines:
            line = line.strip('\n')
            txt.append(line)
        self.txt = txt
        self.name = name
        self.nRows = len(txt) + 2
        self.nCols = len(txt[0]) + 2
        self.grid = []
        for i in range(self.nRows):
            row = []
            for j in range(self.nCols):
                row.append(val)
            self.grid.append(row.copy())

    def __setitem__(self, key, item):
        self.grid[key[0]][key[1]] = item
    
    def __getitem__(self, key):
        return self.grid[key[0]][key[1]]
    
    def printGrid(self):
        with open(self.name + '.txt', 'w') as f:
            for i in range(self.nRows):
                s = ''
                for j in range(self.nCols):
                    s += str(self[(i,j)])
                f.write(s + '\n')

    def copyText(self):
        for i in range(self.nRows - 2 ):
            for j in range(self.nCols - 2):
                self[(i+1,j+1)] = self.txt[i][j]

    def checValidPos(self, pos):
        if pos[0] < 0 or pos[1] < 0 or pos[0] > self.nRows - 1 or pos[1] > self.nCols - 1:
            return False
        return True
    
    def getNeighbours(self, pos, plant):
        neigh = []
        for i in range(4):
            np = self.newPos(pos, i)
            if self.checValidPos(np) and self[np] == plant:
                neigh.append(np)
        return neigh

    def __repr__(self) -> str:
        return self.name

    def newPos(self, pos, rot):
        if rot == 0:
            return (pos[0]-1, pos[1])
        elif rot == 1:
            return (pos[0], pos[1]+1)
        elif rot == 2:
            return (pos[0]+1, pos[1])
        else:
            return (pos[0], pos[1]-1)  

def findField(g: Grid, pos, seen):
    checkPos = [pos]
    plant = g[pos]
    area = 0
    perimeter = 0
    while checkPos:
        pos = checkPos.pop(0)
        perimeter += 4
        area += 1
        n = g.getNeighbours(pos, plant)
        seen.append(pos)
        for neigh in n:
            perimeter -= 1
            if neigh in seen or neigh in checkPos:
                continue
            else:
                checkPos.append(neigh)
    return seen, area, perimeter

def findStart(g: Grid):
    for r in range(g.nRows):
        for c in range(g.nCols):
            if g[(r,c)] == 1:
                return (r,c)

def step(outside, inside, dir, g: Grid):
    newOut = g.newPos(outside, dir)
    newIn = g.newPos(inside, dir)
    # print(left, right)
    # print(outside,'->', newOut,',', inside,'->', newIn,end=' ' )
    side = 0
    if g[newIn] != 1:
        dir += 1
        newOut = newIn
        newIn = inside
        side += 1
    elif g[newOut] == 1:
        dir += 3
        newIn = newOut
        newOut = outside
        side += 1
    # print(newOut, newIn, side)
    return newOut, newIn, dir%4, side


def checkSquare(g: Grid, pos):
    c = []
    dir = 3
    for i in range(4):
        pos = g.newPos(pos, dir)
        if g[pos] == 1:
            c.append(1)
        else:
            c.append(0)
        dir = (dir+1)%4
    if sum(c) == 1 or sum(c) == 3:
        return 1
    if c == [0, 1, 0, 1] or c == [1, 0, 1, 0]:
        return 2
    return 0

def findCorners(g: Grid):
    corners = 0
    for i in range(1, g.nRows):
        for j in range(1, g.nCols):
            pos = (i,j)
            corners += checkSquare(g, pos)
    return corners




def findField2(g: Grid, pos, seen):
    checkPos = [pos]
    plant = g[pos]
    area = 0
    if g[pos] == '.':
        return seen, 0, 0
    while checkPos:
        pos = checkPos.pop(0)
        g[pos] = 1
        area += 1
        n = g.getNeighbours(pos, plant)
        seen.append(pos)
        for neigh in n:
            if neigh in seen or neigh in checkPos:
                continue
            else:
                checkPos.append(neigh)
    corners = findCorners(g)    
    # print(corners)
    g.copyText()
    return seen, area, corners

def part1():
    lines = readFile(1)
    g = Grid(lines)
    g.copyText()
    seen = []
    t = 0
    for i in range(g.nRows):
        for j in range(g.nCols):
            if (i, j) not in seen:
                seen, a, p = findField(g, (i,j), seen)
                t += a*p
    print(t)

def part2():
    lines = readFile(1)
    g = Grid(lines)
    g.copyText()
    g.printGrid()
    seen = []
    t = 0
    for i in range(g.nRows):
        for j in range(g.nCols):
            if (i, j) not in seen:
                seen, a, p = findField2(g, (i,j), seen)
                t += a*p
    print(t)

# part1()
part2()