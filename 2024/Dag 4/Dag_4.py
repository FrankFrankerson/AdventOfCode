
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
    text = []
    for line in lines:
        line = line.strip('\n')
        text.append(line)
    return text

def searchNorth(lineInd, letterInd, lines, word ='MAS', offset=1):
    if lineInd < len(word):
        return 0    
    for i in range(len(word)):
        if lines[lineInd-offset-i][letterInd] != word[i]:
            return 0
    return 1

def searchSouth(lineInd, letterInd, lines, word = 'MAS', offset=1):
    if lineInd > len(lines) - len(word) - 1:
        return 0
    for i in range(len(word)):
        if lines[lineInd+offset+i][letterInd] != word[i]:
            return 0
    return 1

def searchEast(lineInd, letterInd, lines, word = 'MAS', offset=1):
    if letterInd > len(lines[0]) - len(word) - 1:
        return 0
    for i in range(len(word)):
        if lines[lineInd][letterInd+offset+i] != word[i]:
            return 0
    return 1

def searchWest(lineInd, letterInd, lines, word = 'MAS', offset=1):
    if letterInd < len(word):
        return 0
    for i in range(len(word)):
        if lines[lineInd][letterInd-offset-i] != word[i]:
            return 0
    return 1

def searchDiagonal1(lineInd, letterInd, lines, word = 'MAS'):
    # if lineInd < 0 or letterInd < 0 or lineInd > len(lines) - 1 or letterInd > len(lines[0]) - 1:
    #     return 0

    # if lineInd < len(word) or letterInd < len(word)+1:
    #     return 0
    # for i in range(len(word)):
    #     if lines[lineInd-i][letterInd-i] != word[i]:
    #         return 0
    # return 1
    for i in range(len(word)):
        if not checkLetter(lineInd-i, letterInd-i, lines, word[i]):
            return 0
    return 1
    
def searchDiagonal2(lineInd, letterInd, lines, word = 'MAS'):
    # if lineInd < 0 or letterInd < 0 or lineInd > len(lines) - 1 or letterInd > len(lines[0]) - 1:
    #     return 0

    # if lineInd < len(word) or letterInd > len(lines[0]) - len(word)-1:
    #     return 0
    # for i in range(len(word)):
    #     if lines[lineInd-i][letterInd+i] != word[i]:
    #         return 0
    # return 1
    for i in range(len(word)):
        if not checkLetter(lineInd-i, letterInd+i, lines, word[i]):
            return 0
    return 1

def searchDiagonal3(lineInd, letterInd, lines, word = 'MAS'):
    # if lineInd < 0 or letterInd < 0 or lineInd > len(lines) - 1 or letterInd > len(lines[0]) - 1:
    #     return 0

    # if lineInd > len(lines)-len(word) or letterInd < len(word)-1:
    #     return 0
    # for i in range(len(word)):
    #     if lines[lineInd+i][letterInd-i] != word[i]:
    #         return 0
    # return 1
    for i in range(len(word)):
        if not checkLetter(lineInd+i, letterInd-i, lines, word[i]):
            return 0
    return 1

def searchDiagonal4(lineInd, letterInd, lines, word = 'MAS'):
    # if lineInd < 0 or letterInd < 0 or lineInd > len(lines) - 1 or letterInd > len(lines[0]) - 1:
    #     return 0

    # if lineInd > len(lines)-len(word) -1  or letterInd > len(lines[0]) - len(word) -1:
    #     return 0
    
    # for i in range(len(word)):
    #     if lines[lineInd+i][letterInd+i] != word[i]:
    #         return 0
    # return 1
    for i in range(len(word)):
        if not checkLetter(lineInd+i, letterInd+i, lines, word[i]):
            return 0
    return 1

def checkLetter(lineInd, letterInd, lines, letter):
    if lineInd < 0 or letterInd < 0 or lineInd > len(lines) - 1 or letterInd > len(lines[0]) - 1:
        return False
    
    if lines[lineInd][letterInd] == letter:
        return True



def searchWord(lineInd, letterInd, lines, word = 'MAS'):
    n = 0
    n += searchNorth(lineInd, letterInd, lines, word)
    n += searchSouth(lineInd, letterInd, lines, word)
    n += searchEast(lineInd, letterInd, lines, word)
    n += searchWest(lineInd, letterInd, lines, word)
    n += searchDiagonal1(lineInd, letterInd, lines, word)
    n += searchDiagonal2(lineInd, letterInd, lines, word)
    n += searchDiagonal3(lineInd, letterInd, lines, word)
    n += searchDiagonal4(lineInd, letterInd, lines, word)
    return n

def searchWord2(lineInd, letterInd, lines):
    n = 0
    n += searchDiagonal1(lineInd+1, letterInd+1, lines, word = 'MAS')
    n += searchDiagonal2(lineInd+1, letterInd-1, lines)
    n += searchDiagonal3(lineInd-1, letterInd+1, lines)
    n += searchDiagonal4(lineInd-1, letterInd-1, lines)
    if n > 1:
        return 1
    else:
        return 0




def search(lines, letterS = 'X', word='MAS'):
    total = 0
    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            if letter == letterS:
                total += searchWord(i, j, lines, word)
    return total

def search2(lines):
    total = 0
    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            if letter == 'A':
                total += searchWord2(i,j, lines)
    return total

def part1():
    # lines = loadExample()
    lines = loadInput()

    print(search(lines))

    

def part2():
    # lines = loadExample()
    lines = loadInput()

    lines = parseLines(lines)
    print(search2(lines))

# part1()
part2()