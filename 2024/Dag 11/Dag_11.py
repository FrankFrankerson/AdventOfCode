import multiprocessing as mp

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    for i, line in enumerate(lines):
        line = line.strip('\n')
        for j, letter in enumerate(line):
            pass
    
data = {}
def getRock(rock, iteration):
    if iteration == 0:
        return 1
    if (rock, iteration) not in data:
        if rock == 0:
            result = getRock(1, iteration-1)
        elif len(str(rock))%2 == 0:
            rock = str(rock)
            result = 0
            result += getRock(int(rock[:len(rock)//2]), iteration - 1)
            result += getRock(int(rock[len(rock)//2:]), iteration - 1)
        else:
            result = getRock(2024 * rock, iteration - 1)
        data[(rock, iteration)] = result
    return data[(rock,iteration)]
      

def part2():
    lines = readFile(1)
    res = 0
    rocks = [int(x) for x in lines[0].split(' ')]
    for x in rocks:
        res += getRock(x, 75)
    print(res)

# part1()
part2()

