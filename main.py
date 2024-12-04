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

def parseLines(lines):

    reports = []
    for line in lines:
        line = line.strip('\n')
        nums = line.split(' ')
        report = []
        for num in nums:
            if num == '':
                continue
            else:
                report.append(int(num))
        reports.append(report)
    return reports

def searchLeft(line, j):

    j -= 1
    l = ''
    ls = '(lum'
    lp = 0
    while j >= 0:
        t = line[j] 
        if t in '0123456789' and lp == 0:
            l = t + l
        elif t == ls[lp]:
            l = t + l
            lp += 1
            if lp == len(ls):
                return True, l
        else:
            return False, ''
        j -= 1
    return False, ''

def searchRight(line, j):
    j += 1
    r = ''
    seenNum = False
    while j < len(line):
        t = line[j]
        if t in '0123456789':
            r += t
            seenNum = True
        elif t == ')':
            return seenNum, r + ')'
        j+=1
    return False, ''

def walkThroughLine(line):
    for i, t in enumerate(line):
        if t == ',':
            lb, l = searchLeft(line, i)
            if lb:
                rb, r = searchRight(line, r)
                if rb:
                    s = l+r







def part1():
    lines = loadExample()
    # lines = loadInput()

    for line in lines:
        walkThroughLine(line)
    

def part2():
    lines = loadExample()
    # lines = loadInput()



part1()
# part2()