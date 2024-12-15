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
    
    def countBoxes(self):
        count = 0
        for i in range(self.nRows):
            for j in range(self.nCols):
                if self[(i,j)] == '[':
                    count += 1
        return count
    
    def printGrid(self, extra = ''):
        with open(self.name + '_' + extra + '.txt', 'w') as f:
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
    
    def getRobotsPos(self):
        for i in range(self.nRows):
            for j in range(self.nCols):
                if self[(i,j)] == '@':
                    return (i,j)
    
    def calcScore(self):
        score = 0
        for i in range(self.nRows):
            for j in range(self.nCols):
                if self[(i,j)] == 'O' or self[(i,j)] == '[':
                    score += 100*i + j
        return score

    def getDir(self, move):
        if move == '^':
            dir = 0
        elif move == '>':
            dir = 1
        elif move == 'v':
            dir = 2
        elif move == '<':
            dir = 3
        return dir

    def moveItem(self, pos, move):
        dir = self.getDir(move)
        np = self.newPos(pos, dir)
        if self[pos] == '#':
            return False, pos
        elif self[np] == '.':
            self[np] = self[pos]
            self[pos] = '.'
            return True, np
        else:
            res, p = self.moveItem(np, move)
            if res:
                self[np] = self[pos]
                self[pos] = '.'
                return True, np
            else:
                return False, pos
            
    def moveBox(self, p1, dir):
        if self[p1] == '[':
            p2 = (p1[0], p1[1]+1)
        else:
            p2 = (p1[0], p1[1]-1)
        np1 = self.newPos(p1, dir)
        np2 = self.newPos(p2, dir)
        if self[np1] == '#' or self[np2] == '#':
            return 
        if self[np1] in '[]':
            self.moveBox(np1, dir)         
        if self[np2] in '[]':
            self.moveBox(np2, dir)        

        if self[np1] == '.' and self[np2] == '.':
            self[np1] = self[p1]
            self[np2] = self[p2]
            self[p1] = '.'
            self[p2] = '.'

    def checkFreePosition(self, np, dir):
        positionsToCheck = [np]
        while positionsToCheck:
            p = positionsToCheck.pop(0)
            s = self[p]
            if s == '#':
                return False    
            elif s in '[]':
                if s == '[':
                    p2 = (p[0], p[1]+1)
                else:
                    p2 = (p[0], p[1]-1)
                positionsToCheck.append(self.newPos(p, dir))
                positionsToCheck.append(self.newPos(p2, dir))
        return True
            

    def moveItem2(self, pos, move):
        dir = self.getDir(move)
        if dir == 1 or dir == 3:
            _, p = self.moveItem(pos, move)
            return p
        else:
            np = self.newPos(pos, dir)
            if self.checkFreePosition(np, dir):
                if self[np] in '[]':
                    self.moveBox(np, dir)
            else:
                return pos
                        
            if self[np] == '.':
                self[np] = '@'
                self[pos] = '.'
                return np
            else:
                return pos
           
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
    if file == 1:
        fileName = 'input.txt'
    elif file == 0:
        fileName = 'ex_input.txt'
    else:
        fileName = f'ex_input{file}.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    grid = []
    moves = []
    switch = False

    for line in lines:
        line = line.strip('\n')
        if line  == '':
            switch = True
        elif not switch:
            grid.append(line)
        else:
            moves += line
    return grid, moves

def parseLines2(lines):
    grid = []
    moves = []
    switch = False

    for line in lines:
        line = line.strip('\n')
        if line  == '':
            switch = True
        elif not switch:
            nl = ''
            for i in line:
                if i == '#':
                    nl += '##'
                elif i == '.':
                    nl += '..'
                elif i == 'O':
                    nl += '[]'
                elif i == '@':
                    nl += '@.'
            grid.append(nl)
        else:
            moves += line
    return grid, moves

def part1():
    lines = readFile(1)
    grid, moves = parseLines(lines)
    g = Grid(grid)
    g.copyText()

    rPos = g.getRobotsPos()
    for i, move in enumerate(moves):
        # print(rPos, move)
        _, rPos = g.moveItem(rPos, move)
    # g.printGrid(f'final')
    print(g.calcScore())


def part2():
    lines = readFile(1)
    grid, moves = parseLines2(lines)
    g = Grid(grid)
    g.copyText()
    g.printGrid('begin')
    print(f'Boxes start {g.countBoxes()}')

    rPos = g.getRobotsPos()
    for i, move in enumerate(moves):
        # print(rPos, move)
        rPos = g.moveItem2(rPos, move)
        # g.printGrid(f'{i}_{g.getDir(move)}')
    g.printGrid('final')
    print(f'boxes end: {g.countBoxes()}')
    print(g.calcScore())

# part1()
part2()