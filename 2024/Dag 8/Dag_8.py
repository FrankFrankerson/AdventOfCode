import math

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()
    
class Grid:
    def __init__(self, n, m, name='mainGrid', val='.') -> None:
        self.name = name
        self.nRows = n
        self.nCols = m
        self.grid = []
        for i in range(n):
            row = []
            for j in range(m):
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
        
def substractLocs(pos1, pos2):
    return (pos1[0]-pos2[0], pos1[1]-pos2[1])



def parseLines(lines):
    g = Grid(len(lines), len(lines[0]) - 1)
    symbolsLocation= {}
    for i, line in enumerate(lines):
        line = line.strip('\n')
        for j , letter in enumerate(line):
            if letter != '.':
                g[(i,j)] = letter
                if letter in symbolsLocation:
                    symbolsLocation[letter].append((i,j))
                else:
                    symbolsLocation[letter] = [(i,j)]
    return symbolsLocation, g

def countAntinodes(symbolsLoc, grid):
    antiNodeLocs = []
    for sym, locs in symbolsLoc.items():
        # antiNodeLocs[sym] = []
        for i, loc in enumerate(locs):
            for j, loc2 in enumerate(locs):
                if i == j:
                    continue
                if loc[0] == 2:
                    print('here')
                v = substractLocs(loc, loc2)
                signalLoc = (loc[0] - 2*v[0], loc[1] - 2*v[1])
                if grid.checValidPos(signalLoc):
                    if signalLoc not in antiNodeLocs:
                        antiNodeLocs.append(signalLoc)
    return antiNodeLocs

def countAntinodes2(symbolsLoc, grid):
    antiNodeLocs = []
    for sym, locs in symbolsLoc.items():
        # antiNodeLocs[sym] = []
        for i, loc in enumerate(locs):
            for j, loc2 in enumerate(locs):
                if i == j:
                    continue
                v = substractLocs(loc, loc2)
                c = 1
                signalLoc = (loc[0] - c*v[0], loc[1] - c*v[1])
                while grid.checValidPos(signalLoc):
                    if signalLoc not in antiNodeLocs:
                        antiNodeLocs.append(signalLoc)
                    c += 1
                    signalLoc = (loc[0] - c*v[0], loc[1] - c*v[1])
    return antiNodeLocs

def part1():
    lines = readFile(1)
    symbolsLoc, grid = parseLines(lines)
    antiNodeLocs = countAntinodes(symbolsLoc, grid)
    
    # print(sum([len(i) for i in antiNodeLocs.values()]))
    print(antiNodeLocs)
    print(len(antiNodeLocs))

def part2():
    lines = readFile(1)
    symbolsLoc, grid = parseLines(lines)
    antiNodeLocs = countAntinodes2(symbolsLoc, grid)
    
    # print(sum([len(i) for i in antiNodeLocs.values()]))
    print(antiNodeLocs)
    print(len(antiNodeLocs))

# part1()
part2()
