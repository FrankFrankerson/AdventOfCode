with open("input.txt", 'r') as f:
    lines = f.readlines()

possDict = {
    "red" : 12,
    'green': 13,
    'blue': 14
}


def parsePack(pack):
    dict = {'red': 0, 'green': 0, 'blue': 0}

    packs = pack.split(', ')
    for p in packs:
        number, color = p.split(' ')
        dict[color] = int(number)
    return dict

def parseLine(line: str):
    line = line.strip('\n')
    gameId, packs = line.split(": ")
    allPacks = packs.split("; ")
    allDicts = []
    for i in allPacks:
        pp = parsePack(i)
        allDicts.append(pp)
    return allDicts
    #     b = checkPossible(pp)
    #     if not b:
    #         return 0
    # return int(gameId[5:]) 

def checkPossible(packDict):
    for color, num in packDict.items():
        if num > possDict[color]:
            return False
    return True

def checkMin(packDictList: list):
    maxDict = {'red': 0, 'green': 0, 'blue': 0}
    for packDict in packDictList:
        for color, num in packDict.items():
            maxDict[color] = max(num, maxDict[color])
    return maxDict

def calcPower(maxDict):
    num = 1
    for n in maxDict.values():
        num *= n
    return num

def part2():
    s = 0
    for line in lines:
        pl = parseLine(line)
        cm = checkMin(pl)
        po = calcPower(cm)
        s+= po
    print(s)
 
part2()