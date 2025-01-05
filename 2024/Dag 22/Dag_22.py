import collections, math, heapq

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return list(map(lambda x: x.strip('\n'), f.readlines()))


def mix(n, m):
    return n^m

def prune(s):
    return s%16777216

def secretEvolve(s):
    s = prune(mix(s, s*64))
    s = prune(mix(s, s//32))
    s  =prune(mix(s, s*2048))
    return s

def part1():
    data = readFile(1)
    data = list(map(int, data))
    tot = 0
    for i in data:
        s = i 
        for j in range(2000):
            s = secretEvolve(s)
        tot += s
        print(i, s)
    print(tot)

def part2():
    data = readFile(1)
    data = list(map(int, data))
    allMonkData = collections.defaultdict(list)
    # allMonkDiff = collections.defaultdict(list)
    seqMonk = collections.defaultdict(list)
    seqScore = collections.defaultdict(int)
    for m, i in enumerate(data):
        s = i 
        pastSeq = []
        for j in range(2000):
            s = secretEvolve(s)
            v = int(str(s)[-1])
            allMonkData[m].append(v)
            if j > 0:
                pastSeq.append(v-pv)
            if len(pastSeq) == 4:
                seqTuple = tuple(pastSeq)
                if m not in seqMonk[seqTuple]:
                    seqMonk[seqTuple].append(m)
                    seqScore[seqTuple] += v
                pastSeq.pop(0)                
            pv = v
    maxScore = 0
    for i, j in seqScore.items():
        if j > maxScore:
            print(i, j)
            maxScore = j

part2()

