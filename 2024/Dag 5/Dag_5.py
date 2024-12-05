def readFile(inp=0):
    if inp:
        fileName = 'input.txt'
    else:
        fileName ='ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    switch = False
    orderings = {}
    updates = []
    for line in lines:
        line = line.strip('\n')
        if line == '':
            switch = True
            continue
        if switch:
            updates.append(line.split(','))
        else:
            f, s = line.split('|')
            if f in orderings:
                orderings[f].append(s)
            else:
                orderings[f] = [s]
    return orderings, updates

def checkUpdate(update, orderings):
    l = len(update)
    for i, up in enumerate(update[:-1]):
        for j in range(i+1, l):
            if update[j] in orderings and up in orderings[update[j]]:
                return False
    return True

def check(updates, orderings):
    s = 0
    for updat in updates:
        if checkUpdate(updat, orderings):
            s += int(updat[int(len(updat)/2)])
    return s

def checkRemainingUpdate(update, orderings):
    nu = []
    i = 0 
    l = len(update)
    r = update.copy()
    c = r.pop(0)
    while i < l - 1:
        found = False                
        for j in r:
            if j in orderings and c in orderings[j]:
                r.append(c)
                r.remove(j)
                c = j
                found = True
                break
        if not found:  
            nu.append(c)
            c = r.pop(0)
            i+=1
    nu.append(c)
    return nu


def check2(updates, orderings):
    s = 0
    for updat in updates:
        if checkUpdate(updat, orderings):
            continue
        else:
            r = checkRemainingUpdate(updat, orderings)
            s += findMiddle(r)    
            # print(r)
    return s

def findMiddle(update):
    return int(update[int(len(update)/2)])

def part1():
    lines = readFile(1)

    o, u = parseLines(lines)    
    s = check(u, o)
    print(s)

def part2():
    lines = readFile(1)

    o, u = parseLines(lines)    
    s = check2(u, o)
    print(s)

# part1()
part2()