def loadExample():
    with open('ex_input.txt', 'r') as f:
        return f.readlines()

def loadInput(ind=0):
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        if ind:
            return lines[:ind]
        else:
            return lines
        
def parseLine(line):
    line = line.strip('\n')
    cardN, numbers = line.split(': ')
    cardN = cardN.split('Card ')[-1]
    winning, own = numbers.split(' | ')
    winning = winning.split(' ')
    own = own.split(' ')
    while '' in winning:
        winning.remove('')
    while '' in own:
        own.remove('')
    return int(cardN), winning, own
    
def parseLines(lines):
    parsedLines = {}
    for line in lines:
        n, w, o = parseLine(line)
        parsedLines[n] = [w, o]
    return parsedLines

def checkScore(pl):
    w, o = pl
    count = 0
    for c in o:
        if c in w:
            count += 1
    if count > 0:
        return 2**(count-1)
    else:
        return 0
    
def countScore(pl):
    w, o = pl
    count = 0
    for c in o:
        if c in w:
            count += 1
    return count

def part1():
    lines = loadInput()
    pl = parseLines(lines)

    sums = 0
    for n, p in pl.items():
        s = checkScore(p)
        print(n, s)
        sums += s
    print(sums)

def part2():
    lines = loadInput()
    pl = parseLines(lines)
    copies = {}
    for n, p in pl.items():
        s = countScore(p)
        copies[n] = [1, s]

    sums = 0
    for cN, cS in copies.items():
        c, s = cS
        sums += c
        for i in range(s):
            copies[cN + 1 + i][0] += c


    print(sums)    
part2()