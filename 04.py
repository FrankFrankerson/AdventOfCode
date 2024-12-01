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

    l1, l2 = [], []
    for line in lines:
        line = line.strip('\n')
        nums = line.split(' ')
        # print(nums)
        l1.append(int(nums[0]))
        l2.append(int(nums[3]))
    return l1, l2

def calcDistance(l1, l2):
    d = 0
    for i, j in enumerate(l1):
        d += abs(j-l2[i])
    return d

def calcSim(l, r):
    s = 0
    for i, j in enumerate(l):
        s += j*r.count(j)
    return s


def part1():
    # lines = loadExample()
    lines = loadInput()
    l1, l2 = parseLines(lines)
    l1.sort()
    l2.sort()
    print(calcDistance(l1, l2))

def part2():
    # lines = loadExample()
    lines = loadInput()
    l1, l2 = parseLines(lines)
    l1.sort()
    l2.sort()
    print(calcSim(l1, l2))

# part1()
part2()