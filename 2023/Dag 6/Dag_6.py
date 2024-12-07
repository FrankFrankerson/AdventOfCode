import re

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()
    
def parse(lines):
    time = lines[0].split(' ' )
    dist = lines[1].split(' ')

    while '' in time:
        time.remove('')
    
    while '' in dist:
        dist.remove('')

    return time[1:], dist[1:]

def calcDistances(time, distToBeat):
    a = int(time/2)
    b = time-a
    c = 0
    while a*b > distToBeat:
        c += 1
        a -= 1
        b += 1
    
    a = int(time/2)+1
    b = time-a
    while a*b > distToBeat:
        c += 1
        a += 1
        b -= 1

    return c

def part1():
    lines = readFile(1)
    # print(re.findall('/d*',lines[0]))
    times, distances = parse(lines)

    scores = []
    for i, j in enumerate(times):
        scores.append(calcDistances(int(j), int(distances[i])))
    finalScore = 1
    for s in scores:
        finalScore *= s
    print(finalScore)

def part2():
    lines = readFile(1)
    times, distances = parse(lines)
    t = ''
    d = ''
    for i, j in enumerate(times):
        t+= j
        d += distances[i]
    
    print(calcDistances(int(t), int(d)))
    

# part1()
part2()
