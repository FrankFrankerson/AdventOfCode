def readFile(inp=0):
    if inp:
        fileName = 'input.txt'
    else:
        fileName ='ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def checkValidPos(pos, lines):
    if pos[0] < 0 or pos[1] < 0 or pos[0] > len(lines) - 1 or pos[1] > len(lines[0]) - 1:
        return False
    else:
        return True

class Field:

    def __init__(self, s, pos) -> None:
        self.s = s
        self.pos = pos
        self.status = None

    def determineStatus(self, grid, loopParts):
        if self in loopParts:
            self.status = 'X'
        elif self.checkNeighBourHood(grid):
            self.status = 'O'
        return
        # self.status = 'I'

    def checkNeighBourHood(self, grid):
        poss = [[1,0],[-1,0],[0,1],[0,-1]]
        for change_i, change_j in poss:
            n = self.pos.copy()
            n[0] -= change_i
            n[1] -= change_j
            if not checkValidPos(n, grid):
                return True
            if grid[n[0]][n[1]].status == 'O':
                return True
        return False

    def forward(self, dir):
        update = self.pos.copy()
        if self.s == '-':
            if dir == 1:
                update[1] += 1
            elif dir == 3:
                update[1] -= 1
        elif self.s == "|":
            if dir == 2:
                update[0] += 1
            elif dir == 0:
                update[0] -= 1
        elif self.s == 'F':
            if dir == 0:
                update[1] += 1
                dir = 1
            elif dir == 3:
                update[0] += 1
                dir = 2
        elif self.s == '7':
            if dir == 1:
                update[0] += 1
                dir = 2
            elif dir == 0:
                update[1] -= 1
                dir = 3
        elif self.s == 'L':
            if dir == 3:
                update[0] -= 1
                dir = 0
            elif dir == 2:
                update[1] += 1
                dir = 1
        elif self.s == 'J':
            if dir == 1:
                update[0] -= 1
                dir = 0
            elif dir == 2:
                update[1] -= 1
                dir = 3
        elif self.s == 'S':
            if dir == 0:
                update[0] -= 1
            elif dir == 1:
                update[1] += 1
            elif dir == 2:
                update[0] += 1
            elif dir == 3:
                update[1] -= 1
        else:
            return update, dir, False
        return update, dir, not(update == self.pos)

    def __eq__(self, pos):
        if self.pos[0] == pos[0] and self.pos[1] == pos[1]:
            return True
        return False

    def __repr__(self) -> str:
        return f'({self.pos[0]}, {self.pos[1]})'

def buildGrid(lines):
    grid = []
    for i, line in enumerate(lines):
        line = line.strip('\n')
        row = []
        for j, s in enumerate(line):
            f = Field(s, [i,j])
            if f.s == 'S':
                start = [i,j]
            row.append(f)
        grid.append(row.copy())
    return grid, start

def traverseGrid(grid, start):
    spos: Field = grid[start[0]][start[1]]
    foundLoop = False
    sdir = 0
    while not foundLoop and sdir < 4:
        steps = 0
        loopPart = []
        pos, dir, updated = spos.forward(sdir)
        while updated:
            if checkValidPos(pos, grid):
                loopPart.append(pos)
                steps += 1
                if pos == start:
                    foundLoop = True
                    updated = False
                else:
                    pos, dir, updated = (grid[pos[0]][pos[1]]).forward(dir)
            else:
                updated = False
        sdir += 1
    return steps, loopPart.copy()

def countInside(loopParts, grid):
    allFields = []
    for r in grid:
        for f in r:
            allFields.append(f)

    f: Field
    c = 0
    while allFields != [] and c!= len(allFields):
        f = allFields.pop(0)
        if not f.status:
            f.determineStatus(grid, loopParts)
            if not f.status:
                c += 1
                allFields.append(f)
            else:
                c = 0
    return len(allFields)        

def writeToFile(grid, fileName = 'pipes.txt', drawPipe=True):
    with open(fileName, 'w') as file:
        for r in grid:
            rowDraw = ''
            for f in r:
                if drawPipe:
                    if f.status == 'X':
                        rowDraw += f.s
                    else:
                        rowDraw += '.'
                elif f.status:
                    rowDraw += f.status
                else:
                    rowDraw += 'I'
            file.write(rowDraw+'\n')
    
def determineInside(grid, loopParts):
    inside = []
    for r in grid:
        c = 0
        f: Field
        for f in r:
            if f in loopParts:
                f.status = 'X'
                if f.s in ['|', 'S']:
                    c += 1
                elif f.s in ['F', 'J']:
                    c += 0.5
                elif f.s in ['7','L']:
                    c -= 0.5
            elif c%2 == 1:
                f.status = 'I'
                inside.append(f)
            else:
                f.status = 'O'
    return inside

def part1():
    lines = readFile()
    # lines = readFile(1)
    grid, start = buildGrid(lines)
    steps, _ = traverseGrid(grid, start)
    print(steps/2)

def part2():
    # lines = readFile(0)
    lines = readFile(1)
    grid, start = buildGrid(lines)
    steps, loop = traverseGrid(grid, start)

    ret = determineInside(grid, loop)
    print(len(ret))
    # print(countInside(loop, grid))
    writeToFile(grid, drawPipe=True)


# part1()
part2()
