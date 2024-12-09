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