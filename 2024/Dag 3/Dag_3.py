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
        else:
            return False, ''
        j+=1
    return False, ''

def evaluateMul(s):
    nums = s[4:-1]
    nums = nums.split(',')
    return int(nums[0])*int(nums[1])

def walkThroughLine(line):
    s = 0
    for i, t in enumerate(line):
        if t == ',':
            lb, l = searchLeft(line, i)
            if lb:
                rb, r = searchRight(line, i)
                if rb:
                    s += evaluateMul(l+','+r)
    return s

def sL(sec):
    i = len(sec) - 1
    n = ''
    seenNum = False
    while i >= 0:
        if sec[i] in '0123456789':
            n = sec[i] + n
            seenNum = True
        elif sec[i] == '(':
            try:
                if 'mul' == sec[i-3:i]:
                    return seenNum, n
                else:
                    return False, n
            except:
                return False, n
        else:
            return False, n
        i -= 1
    return False, n

def sR(sec):
    i = 0
    seenNum = False
    n = ''
    while i < len(sec):
        if sec[i] in '0123456789':
            seenNum = True
            n += sec[i]
        elif sec[i] == ')':
            return seenNum, n
        else:
            return False, ''
        i+=1
    return False, ''

def walktroughLine2(line):
    sections = line.split(',')
    s = 0
    for i, sec in enumerate(sections[:-1]):
        bl, l = sL(sec)
        if bl:
            br, r = sR(sections[i+1])
            if br:
                # print(l, r, sec[-6:] + ',' + sections[i+1][:4])
                s += int(l)*int(r)
    return s



def wtLine2(line: str, do=False):
    sections = line.split("don\'t()")
    
    print(len(sections))

    # for sec in sections:
        # print(sec)
    s = 0
    for sec in sections:
        secs = sec.split('do()')
        for sec2 in secs:
            if do:
                s+=walktroughLine2(sec2)
            do = True
        do = False
    return s

def part1():
    lines = loadExample()
    # lines = loadInput()

    s = 0
    for line in lines:
        s += walktroughLine2(line)
    print(s)
    

def part2():
    # lines = loadExample()
    lines = loadInput()
    text = ''
    for line in lines:
        text += line.strip('\n')
    s = 0
    
    s += wtLine2(text, True)
    print(s)



# part1()
part2()