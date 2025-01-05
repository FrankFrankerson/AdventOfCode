import collections

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return list(map(lambda x: x.strip('\n'), f.readlines()))
    

def parseLines(lines, swap = []):
    switch = False
    initial = {}
    logic = []
    allEnd = set()
    for i in lines:
        if i == '':
            switch = True
            continue
        elif not switch:
            p, v  = i.split(': ')
            initial[p] = int(v)
        else:
            p1, comm, p2, arr, p3 = i.split(' ')
            for (s1, s2) in swap:
                if p3 == s1:
                    p3 = s2
                elif p3 == s2:
                    p3 = s1
            logic.append((p1, p2, comm, p3))
            allEnd.add(p3)
    return initial, logic, allEnd

def runLogic(initial, logic, allEnd):
    setValues = initial
    done = set()

    while not all(x in setValues for x in allEnd):
        sl = len(setValues)
        for (p1, p2, comm, p3) in logic:
            if (p1, p2, comm, p3) in done: continue
            if p1 not in setValues or p2 not in setValues: continue
            if comm == 'OR':
                if setValues[p1] or setValues[p2]:
                    setValues[p3] = 1
                else:
                    setValues[p3] = 0
            elif comm == 'XOR':
                if setValues[p1] != setValues[p2]:
                    setValues[p3] = 1
                else:
                    setValues[p3] = 0
            elif comm == 'AND':
                if setValues[p1] and setValues[p2]:
                    setValues[p3] = 1
                else:
                    setValues[p3] = 0
            done.add((p1, p2, comm, p3))
        se = len(setValues)
        if se == sl:
            break
    return setValues

def solution(endVals: dict):
    zVals = {}
    for i,j in endVals.items():
        if i[0] == 'z' and i[1] in '0123456789':
            zVals[i] = j
    sVals = dict(sorted(zVals.items(), reverse=True))
    num = ''.join(str(x) for x in sVals.values())
    return num
    
def testCase1(xVals, yVals):
    x = len(xVals)%2
    y = len(yVals)%2+1
    i = len(xVals) - 3
    while i > 0:
        x += 2**i
        y += 2**(i+1)  
        i -= 2
    return x,y

def testCase2(xVals, yVals):
    y = int('1'*len(yVals), 2)
    return 0, y

def testCase3(xVals, yVals):
    x = int('1'*len(xVals), 2)
    return x, 0

def tryNums(x, y, xVals, yVals, logic, allEnd):
    zVals = []
    for i in allEnd:
        if i[0] == 'z':
            zVals.append(i)
    z = x + y
    xBin = bin(x)[2:].zfill(len(xVals))
    yBin = bin(y)[2:].zfill(len(yVals))
    zBin = bin(z)[2:].zfill(len(zVals))
    initial = {}
    for i, j in enumerate(xVals):
        initial[j] = xBin[i]
    for i, j in enumerate(yVals):
        initial[j] = yBin[i]
    # print(initial)
    endVals = runLogic(initial, logic, allEnd)
    endZ = solution(endVals)
    # print(zBin, endZ)
    return zBin == endZ

def runAddition(initial, logic, allEnd):
    xVals = []
    yVals = []
    for x in initial:
        if x[0] == 'x':
            xVals.append(x)
        elif x[0] == 'y':
            yVals.append(x)
    # print(len(xVals), len(yVals))
    x1, y1 = testCase1(xVals, yVals)
    x2, y2 = testCase2(xVals, yVals)
    x3, y3 = testCase3(xVals, yVals)

    casesFailed = [False, False, False]
    newLogic = logic.copy()
    tried = []
    while not all(casesFailed):
        newLogic, tried, swapped = changeLogic(logic, tried)
        casesFailed[0] = tryNums(x1, y1, xVals, yVals, newLogic, allEnd)
        casesFailed[1] = tryNums(x2, y2, xVals, yVals, newLogic, allEnd)
        casesFailed[2] = tryNums(x3, y3, xVals, yVals, newLogic, allEnd)
        print(casesFailed)

def changeLogic(logic: list, tried = []):
    def checkValid(s1, s2):
        for (p1, p2) in swappers:
            if p1 == s1 or p1 == s2 or p2 == s1 or p2 == s2: return False
            if (s1, s2) in tried: return False
        return True

    newLogic = logic.copy()
    swappers = []
    l = len(logic)
    sp1 = 0
    while len(swappers) < 4:
        p1 = 0
        p2 = 1
        while not checkValid(p1, p2) :
            p2 += 1
            if p2 == l:
                p1 += 1
                p2 = p1 + 1
        swappers.append((p1, p2))
        tried.append((p1, p2))
        tried.append((p2, p1))
    print(swappers)
    for (s1, s2) in swappers:
        (p1, p2, comm, p3) = newLogic.pop(s2)
        (p11, p22, comm2, p33) = newLogic.pop(s1)
        newLogic.insert(s1, (p1, p2, comm, p33))
        newLogic.insert(s2, (p11, p22, comm2, p3))
    return newLogic, tried, swappers

def printLogicTree(val, logic, endVal=None):
    pq = [(0, val)]
    retVal = []
    while pq:
        indent, v = pq.pop()
        # if v in retVal:
        #     print(v)
        retVal.append(v)

        if v[0] in 'xy': 
            continue
            # print('-'*indent + f'{v}')
        for (p1, p2, comm, p3) in logic:
            if p3 == v:
                # print('-'*indent + f'{p1} {comm} {p2} --> {p3}')
                pq.append((indent + 1, p1))
                pq.append((indent+1,p2))
    return sorted(retVal)

def getInputs(logic, allEnd):
    zVals = []
    i: str
    for i in allEnd:
        if i.startswith('z'):
            zVals.append(i)
    
    zVals = sorted(zVals)
    touched = {}
    for i in zVals:
        r = printLogicTree(i, logic)
        touched[i] = r
    
    return touched

def traceInput(v, logic):
    trace = set()

    pq = [v]
    while pq:
        val:str = pq.pop()
        trace.add(val)
        if val.startswith('z'):
            continue
        for (p1, p2, comm, p3) in logic:
            if p1 == val or p2 == val:
                pq.append(p3)
    return sorted(trace)


lines = readFile(1)
swappers = [
    ('z18', 'jct')
]
initial, logic, allEnd = parseLines(lines, swap=swappers)
# runAddition(initial, logic, allEnd)

def getTouched(logic, allend):
    touc = getInputs(logic, allEnd)
    for i, j in touc.items():
        integer = int(i[1:])
        for k in range(integer+1):
            if f'x{str(k).zfill(2)}' not in j:
                print(i, 'missing', f'x{str(k).zfill(2)}')
            if f'y{str(k).zfill(2)}' not in j:
                print(i, 'missing', f'y{str(k).zfill(2)}')

def countOccurences(li):
    ret = collections.defaultdict(int)
    for l in li:
        ret[l] += 1
    return ret

# revTrace = printLogicTree('z18', logic)
revTrace = printLogicTree('z19', logic)
# trac = traceInput('x00', logic)
print(revTrace)

print(countOccurences(revTrace))
# print(trac)

# getTouched(logic, allEnd)



    # print(i, j)

# printLogicTree('z12', logic)

# endVals = runLogic(initial, logic, allEnd)
# solution(endVals)
# for i in sorted(endVals.items()):
#     print(i)