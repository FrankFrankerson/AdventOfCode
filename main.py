class Grid:
    def __init__(self, lines, name='mainGrid', val='.') -> None:
        txt = []
        for line in lines:
            line = line.strip('\n')
            txt.append(line)
        self.txt = txt
        self.name = name
        self.nRows = len(txt)
        self.nCols = len(txt[0])
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
        for i in range(self.nRows):
            for j in range(self.nCols):
                self[(i,j)] = self.txt[i][j]

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
    for i, line in enumerate(lines):
        line = line.strip('\n')
        for j, letter in enumerate(line):
            pass
    

def part1():
    lines = readFile()


def part2():
    lines = readFile()

part1()
# part2()