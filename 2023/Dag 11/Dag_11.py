from multiprocessing import Pool, Process, cpu_count

def readFile(inp=0, fileName=None):
    if inp:
        fileName = 'input.txt'
    elif fileName:
        fileName = fileName
    else:
        fileName ='ex_input.txt'
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
            np = newPos(pos, i)
            if self.checValidPos(np):
                neigh.append(np)
        return neigh

    def __repr__(self) -> str:
        return self.name

def newPos(pos, rot):
    if rot == 0:
        return (pos[0]-1, pos[1])
    elif rot == 1:
        return (pos[0], pos[1]+1)
    elif rot == 2:
        return (pos[0]+1, pos[1])
    else:
        return (pos[0], pos[1]-1)

class Galaxy(Grid):
    def __init__(self, i, j, n, rows, cols) -> None:
        super().__init__(rows, cols, name=f'Gal_{n}', val=-1)
        self.n = n
        self.pos = (i,j)
        # self.grid = Grid(rows, cols, name=f'Gal_{n}', val=-1)

    def doSP(self, emptyRows, emptyCols):
        q = [(self.pos)]
        s = []
        while q != []:
            pos = q.pop(0)
            s.append(pos)
            # print(f'Gal_{self.n}:',len(s)/self.nRows*self.nCols)
            val = 1
            if pos[0] in emptyRows:
                val += 1
            if pos[1] in emptyCols:
                val += 1
            self[pos] += val
            for n in self.getNeighbours(pos):
                if n not in q and n not in s:
                    self[n] = self[pos]
                    q.append(n)
        # self.printGrid()         
       

def parseLines(lines):
    rows = len(lines)
    cols = len(lines[0])-1
    grid = Grid(rows, cols)
    emptyRows = []
    emptyCols = []
    for i in range(cols):
        emptyCols.append(i)
    galaxies = []
    for i, line in enumerate(lines):
        line = line.strip('\n')
        if line.find('#') < 0:
            emptyRows.append(i)
        else:
            for j, sym in enumerate(line):
                if sym == '#':
                    grid[(i, j)] = len(galaxies)
                    g = Galaxy(i, j, len(galaxies), rows, cols)
                    galaxies.append(g)
                    if j in emptyCols:
                        emptyCols.remove(j)
    return grid, emptyRows, emptyCols, galaxies


def part1():
    lines = readFile(1)
    grid, emptyRows, emptyCols, galaxies = parseLines(lines)
    grid.printGrid()
    g: Galaxy
    processes = []
    processors = cpu_count()-1
    for i, g in enumerate(galaxies):
        # print(f'{(i+1)/len(galaxies):.2}')
        p = Process(target=g.doSP, args=(emptyRows, emptyCols))
        processes.append(p)

    started = []
    finished = 0
    while processes != []:
        if len(started) < processors:
            p = processes.pop()        
            p.start()
            started.append(p)
        else:
            print(finished/len(galaxies))
            p = started.pop(0)
            p.join()
            finished += 1
    while started != []:
        p = started.pop(0)
        p.join()

    s = 0
    for i, g in enumerate(galaxies[:-1]):
        for g2 in galaxies[i+1:]:
            s += g[g2.pos]
    print(s)

if __name__ == "__main__":
    part1()