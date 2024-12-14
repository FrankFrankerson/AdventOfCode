def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    data = []
    for i, line in enumerate(lines):
        line = line.strip('\n')
        sp, re = line.split(' ')
        data.append([sp, re])
    return data

cache = {}
def recFunc(sp: str, rec):
    h = sp.count('#')
    q = sp.count('?')
    if len(rec) == 1:
        cache[(sp, rec)] = checkSpring(sp, int(rec))
    elif q == 0:
        cache[(sp, rec)] =  controleer(sp, rec)
    else:
        t = 0
        ns1 = sp.replace('?', '#', 1)
        ns2 = sp.replace('?', '.', 1)
        t += recFunc(ns1, rec)
        t += recFunc(ns2, rec)
        cache[sp] = t
    return cache[(sp, rec)]

def controleer(sp, record):
    parts = getParts(sp)
    recParts = record.split(',')
    if len(parts) != len(recParts):
        return 0
    else:
        for i in range(len(parts)):
            if parts[i].count('#') != int(recParts[i]):
                return 0
        return 1

def checkSpring(spring, n):
    l = len(spring)
    i = 0
    count = 0
    while i < l - n + 1:
        s = spring[i:i+n]
        if s.count('.') == 0:
            count += 1
        i += 1
    return count

def getParts(sp):
    allParts = sp.split('.')
    parts = []
    for p in allParts:
        if p:
            parts.append(p)
    return parts
   

def part1():
    lines = readFile()

    r = recFunc('.??..??...?##.','1,1,3')
    print(r)


def part2():
    lines = readFile()

part1()
# part2()