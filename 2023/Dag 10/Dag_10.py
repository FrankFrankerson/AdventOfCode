def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()
  

class Field:
    def __init__(self, s):
        self.s = s
        self.north = False
        self.east = False
        self.south = False
        self.west = False
        self.handleS()

    def handleS(self):
        if self.s == '.':
            pass
        elif self.s == '|':
            self.north = True
            self.south = True
        elif self.s == 'F':
            self.east = True
            self.south = True
        elif self.s == '-':
            self.west = True
            self.east = True
        elif self.s == 'L':
            self.north = True
            self.east = True
        elif self.s == 'J':
            self.north = True
            self.west = True
        elif self.s == '7':
            self.west = True
            self.south = True
        elif self.s == 'S':
            self.north = True
            self.east = True
            self.south = True
            self.west = True

    def __repr__(self):
        return self.s


def handleLines(lines):
    plane = []
    start = (0,0)
    for j, line in enumerate(lines):
        line = line.strip('\n')
        row = []
        for i, s in enumerate(line):
            f = Field(s)
            row.append(f)
            if f.s == 'S':
                start = (j, i)
        plane.append(row.copy())
    return plane, start

def 

def part1():
    lines = readFile()
    plane, start = handleLines(lines)
    print(plane)

part1()