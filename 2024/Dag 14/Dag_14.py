class Grid:
    def __init__(self, nRows, nCols, name='mainGrid', val='.') -> None:
        self.name = name
        self.nRows = nRows
        self.nCols = nCols
        self.grid = []
        self.seenRobots = 0
        self.middelRobots = 0
        for i in range(self.nRows):
            row = []
            for j in range(self.nCols):
                row.append(val)
            self.grid.append(row.copy())

    def checkChristmasTree(self):
        score = 0
        mC = self.nCols//2
        mR = self.nRows // 2
        # colscore > 31
        colScores = [0]*self.nCols
        for i in range(self.nRows):
            rowScore = 0
            for j in range(self.nCols-1):
                if self[(i,j)] != '.':
                    rowScore += 1
                    colScores[j] += 1
            if rowScore > 30:
                score += 1
        if max(colScores) > 31:
            score += 1
        return score


    def __setitem__(self, key, item):
        self.grid[key[0]][key[1]] = item
    
    def __getitem__(self, key):
        return self.grid[key[0]][key[1]]
    
    def printGrid(self, extra=''):
        with open(self.name + extra + '.txt', 'w') as f:
            for i in range(self.nRows):
                s = ''
                for j in range(self.nCols):
                    s += str(self[(i,j)])
                f.write(s + '\n')

    def getRobotsPerQuadrant(self):
        res = [0]*5
        mC = self.nCols//2
        mH = self.nRows//2
        for i in range(self.nRows):
            for j in range(self.nCols):
                if self.grid[i][j] != '.':
                    
                    if i < mH and j < mC:
                        q = 0
                    elif i > mH and j < mC:
                        q = 1
                    elif i < mH and j > mC:
                        q = 2
                    elif i > mH and j > mC:
                        q = 3
                    else:
                        q = 4
                    res[q] += self.grid[i][j]
        return res

    def checValidPos(self, pos):
        if pos[0] < 0 or pos[1] < 0 or pos[0] > self.nRows - 1 or pos[1] > self.nCols - 1:
            return False
        return True
    
    def getNeighbours(self, pos):
        neigh = []
        for i in range(4):
            np = self.newPos(pos, i)
            if self.checValidPos(np):
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

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    txt = map(lambda x: x.strip('\n'), lines) 
    data = []
    for i, l in enumerate(txt):
        p, v = l.split()
        _, p = p.split('=')
        p1, p2 = map(int, p.split(','))
        _, v = v.split('=')
        v1, v2 = map(int, v.split(','))
        data.append([(p2, p1), (v2, v1)])
    return data

def calcRobot(p, v, w, t, s):
    endP = (0,0)
    # if v[0] > 0 and v[1] > 0:   
    endP = ((p[0]+s*v[0])%t, (p[1]+s*v[1])%w)
    return endP

def part1():
    lines = readFile(1)
    data = parseLines(lines)
    
    w = 101
    t = 103
    g1 = Grid(t, w, 'before')
    print(data)
    seen = 0
    for i in range(10000):
        endPositions = []
        g = Grid(t,w, name=f'Iter {i}')
        for p, v in data:
            if g1[p] == '.':
                g1[p] = 1
            else:
                g1[p] += 1
            endPositions.append(calcRobot(p, v, w,t,i+1))
        for p in endPositions:
            if g[p] == '.':
                g[p] = 1
            else:
                g[p] += 1
        r = g.checkChristmasTree()
        if r > 2:
            g.printGrid()

    # g1.printGrid()
    # rQ = g.getRobotsPerQuadrant()
    # tot = 1
    # for i in rQ[:-1]:
    #     tot*=i
    # print(tot)


def part2():
    lines = readFile()

part1()
# part2()