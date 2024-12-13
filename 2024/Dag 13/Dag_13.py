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

import numpy as np
import math

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    data = []
    curr = []
    for i, line in enumerate(lines):
        line = line.strip('\n')
        if i%4 < 2:
            _, txt = line.split(': ')
            x_info, y_info = txt.split(', ')
            _ , x_info = x_info.split('+')
            _, y_info = y_info.split('+')
            curr.append((int(x_info), int(y_info)))
        elif i%4 == 2:
            _, info = line.split(': ')
            x_info, y_info = info.split(', ')
            _ , x_info = x_info.split('=')
            _, y_info = y_info.split('=')
            curr.append((int(x_info), int(y_info)))
        elif i%4 == 3:
            data.append(curr.copy())
            curr = []
    if curr:
        data.append(curr)
    return data


def addVector(v1, v2, mult=1):
    return (v1[0]+v2[0]*mult, v1[1]+v2[1]*mult)

def checkVector(v1, v2):
    if v2[0]-v1[0] < 0 or v2[1]-v1[1] < 0:
        return False
    return True

def findSmallestVector(v1):
    m1 = math.gcd(v1[0], v1[1])
    return (v1[0]//m1, v1[1]//m1), m1

def checkMultiple(v1, v2):
    if v1[0]%v2[0] == 0:
        m = v1[0]//v2[0]
        if v2[1]*m == v1[1]:
            return True
    return False

def getPrize2(a_vector, b_vector, prize_loc, addLoc=0):
    addLoc = 10000000000000
    checkLoc = (addLoc+prize_loc[0], addLoc+prize_loc[1])
    # smallestV, multiplier = findSmallestVector(checkLoc)
    # if checkMultiple(a_vector, b_vector) or checkMultiple(b_vector, a_vector):
    #     print('doSome')
    # else:
    m = np.array([a_vector, b_vector])
    v = np.array(checkLoc)
    m = np.transpose(m)
    r = np.linalg.solve(m, v)
    # print(r)
    a_count = round(r[0])
    b_count = round(r[1])
    ret = addVector((0,0), a_vector, a_count)
    ret = addVector(ret, b_vector, b_count)
    if ret == checkLoc:
        # real = getPrize(a_vector, b_vector, prize_loc)
        return a_count, b_count
    return 0, 0

def getPrize(a_vector, b_vector, prize_loc):
    a_count = 0
    bx_steps = prize_loc[0]//b_vector[0]
    by_steps = prize_loc[1]//b_vector[1]
    b_count = min(bx_steps, by_steps)
    curr_loc = (b_count*b_vector[0], b_count*b_vector[1])
    while a_count<101:
        if curr_loc == prize_loc and b_count < 101:
            break
        curr_loc = addVector(curr_loc, a_vector)
        a_count += 1
        while curr_loc[0] > prize_loc[0] or curr_loc[1] > prize_loc[1]:
            curr_loc = addVector(curr_loc, b_vector, -1)
            b_count -= 1
        
    if a_count > -1 and a_count < 101 and b_count > -1 and b_count < 101:
        return a_count, b_count
    return 0,0

def part1():
    lines = readFile(1)

    data = parseLines(lines)
    tot = 0
    for d in data:
        ret = getPrize(d[0], d[1], d[2])
        tot += ret[0]*3 + ret[1]
    print(tot)

    # print(data)


def part2():
    lines = readFile(1)

    data = parseLines(lines)
    tot = 0
    for i, d in enumerate(data):
        # ret1 = getPrize(d[0], d[1], d[2])
        ret2 = getPrize2(d[0], d[1], d[2])
        # if ret1 != ret2 and ret1 != (0,0):
        #     print(i, d[-1], ret1, ret2)
        tot += ret2[0]*3 + ret2[1]
    print(tot)

# part1()
part2()

# v1 = np.array([[94, 22], [34, 67]])
# v2 = np.array([8400, 5400])
# r = np.linalg.solve(v1,v2)
# print(type(r[0]))

# r = addVector((0,0), (94,34), 80)
# r = addVector(r, (22,67), 40)
# r = getPrize((94,34), (22,67), (8400,5400))
# r = getPrize((1,1), (2,2), (6,6))
# r = checkMultiple((1,1), (2,2))
# print(r)
# print(2%1)
# r = findSmallestVector((9,4))
# # r = checkMultiple((2,2), (1,3))
# print(r)