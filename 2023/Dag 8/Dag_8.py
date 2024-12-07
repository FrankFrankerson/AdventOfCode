import math

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()
    

class Node:

    def __init__(self, line):
        line = line.strip('\n').split(' = ')
        self.name = line[0]
        l, r = line[1][1:-1].split(', ')
        self.visited = [False, False]
        self.dir = [l, r]
    
    def __repr__(self):
        return f'{self.name}: ({self.left}, {self.right})'
    
    def getDirection(self, ins):
        dir = 0 if ins=='L' else 1
        return self.dir[dir]
        # if self.visited[dir]:
        #     return self.dir[not(dir)]
        # else:
        #     self.visited[dir] = True
        #     return self.dir[dir]

def createNodes(lines):
    n = {}
    for line in lines:
        node = Node(line)
        n[node.name] = node
    return n

def checkNodes(nodes):
    for n in nodes:
        if n[-1] != 'Z':
            return False
    return True

def followNode(node, nodes, instructions, iptr):
    steps = 0
    currNode = node
    while currNode[-1] != 'Z':
        steps += 1
        currNode = nodes[currNode].getDirection(instructions[iptr])
        iptr += 1
        if iptr == len(instructions):
            iptr = 0
    return steps, iptr, currNode

def part1():
    lines = readFile(1)

    instructions = lines[0].strip('\n')
    nodes = createNodes(lines[2:])

    currNode = "AAA"
    iptr = 0
    steps = 0
    while currNode != 'ZZZ':
        steps += 1
        currNode = nodes[currNode].getDirection(instructions[iptr])
        iptr += 1
        if iptr == len(instructions):
            iptr = 0
    print(steps)

# part1()

def part2():
    lines = readFile(1)
    instructions = lines[0].strip('\n')
    nodes = createNodes(lines[2:])

    startingNodes = []
    for n in nodes:
        if n[-1] == 'A':
            startingNodes.append(n)

    iptr = 0
    totalSteps = 0
    res = []
    for n in startingNodes:
        ret = followNode(n, nodes, instructions, iptr)
        res.append(ret[0])
    print(math.lcm(*res))
    

part2()