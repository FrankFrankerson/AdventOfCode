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
    
def createActiveMatrix(lines):
    active = {}
    for lineInd in range(1, len(lines)):
        line = lines[lineInd].strip('\n')
        for ind, i in enumerate(line):
            if i in ".0123456789":
                pass
            else:
                for j in range(lineInd-1, lineInd+2):
                    if j in active:
                        active[j].append(max(0, ind-1))
                        active[j].append(ind)
                        active[j].append(min(ind+1, len(lines)))
                    else:
                        active[j] = [max(0, ind-1), ind, min(ind+1, len(line))].copy()

    retActive = {}
    for i, j in active.items():
        retActive[i] = set(j)
    return retActive

def createActiveMatrixException(lines, symb='*'):
    active = {}
    for lineInd in range(1, len(lines)):
        line = lines[lineInd].strip('\n')
        for ind, i in enumerate(line):
            if i in symb:
                for j in range(lineInd-1, lineInd+2):
                    if j in active:
                        active[j].append(max(0, ind-1))
                        active[j].append(ind)
                        active[j].append(min(ind+1, len(lines)))
                    else:
                        active[j] = [max(0, ind-1), ind, min(ind+1, len(line))].copy()

    retActive = {}
    for i, j in active.items():
        retActive[i] = set(j)
    return retActive


def findPartNr(lines, activeMatrix):
    partNr = {}
    for i, line in enumerate(lines):
        line = line.strip('\n')
        number = ''
        addNumber = False
        for j, s in enumerate(line):
            if s in '0123456789':
                number += s
                if j in activeMatrix[i]:
                    addNumber=True
            elif number and addNumber:
                if i in partNr:
                    partNr[i].append(int(number))
                else:
                    partNr[i] = [int(number)]
                addNumber = False
                number = ''
            else:
                number = ''
        if number and addNumber:
            if i in partNr:
                partNr[i].append(int(number))
            else:
                partNr[i] = [int(number)]
    return partNr

def searchArea(lineInd, letterInd, maxLengt, maxLine):
    area = []
    for i in range(3):
        if maxLengt >= lineInd-1+i >=0:
            for j in range(3):
                if maxLine >= letterInd-1+j >= 0:
                    area.append([lineInd-1+i ,letterInd-1+j])
    return area

def completeNumber(line, ind, li):
    while ind >= 0 and line[ind] in '0123456789':
        ind -= 1
    num = ''
    ind += 1
    indices = []
    while ind < len(line) and line[ind] in '0123456789':
        num += line[ind]
        indices.append([li, ind])
        ind += 1
    return int(num), indices
                

def searchGear(lines, searchArea):
    nums = []
    while searchArea != []:
        l,i = searchArea.pop()
        if lines[l][i] in '0123456789':
            num, indices = completeNumber(lines[l], i, l)
            for ind in indices:
                if ind in searchArea:
                    searchArea.remove(ind)
            nums.append(num)
    if len(nums) == 2:
        return nums[0]*nums[1]    
    else:
        return 0


def findGear(lines):
    sums = 0
    for lineInd, line in enumerate(lines):
        for letterInd, s in enumerate(line):
            if s == '*':
                n = searchGear(lines, searchArea(lineInd, letterInd, len(lines), len(line)))
                sums += n
    return sums

def part1():
    lines = loadInput()
   
    am = createActiveMatrix(lines)
    pn = findPartNr(lines, am)
    s = 0
    for i in pn.values():
        s += sum(i)
    print(s)

def part2():
    lines = loadInput()
    print(findGear(lines))

# part1()
part2()
