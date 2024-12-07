def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()
    
class Hand:
    def __init__(self, handStr, bid):
        self.hand = handStr
        self.d = changeHand(handStr)
        self.type = checkHand(self.d)
        self.bid = int(bid)

    def __repr__(self):
        return f'{self.hand}'
    
    def __lt__(self, other):
        if self.type == other.type:
            for i, j in enumerate(self.hand):
                if j == other.hand[i]:
                    continue
                else:
                    c2 = other.hand[i]
                    if j in '23456789':
                        if c2 in '23456789':
                            return int(j) < int(c2)
                        else:
                            return True
                    else:
                        if c2 in '23456789':
                            return False
                        else:
                            return 'TJQKA'.find(j) < 'TJQKA'.find(c2)

        else:
            return self.type < other.type


class Hand2:
    def __init__(self, handStr, bid):
        self.hand = handStr
        self.d = changeHand(handStr)
        self.type = checkHand2(self.d)
        self.bid = int(bid)

    def __repr__(self):
        return f'{self.hand}'
    
    def __lt__(self, other):
        if self.type == other.type:
            for i, j in enumerate(self.hand):
                c2 = other.hand[i]
                if j == other.hand[i]:
                    continue
                if j == 'J':
                    return True
                if c2 == 'J':
                    return False
                if j in '23456789':
                    if c2 in '23456789':
                        return int(j) < int(c2)
                    else:
                        return True
                if c2 in '23456789':
                    return False
                order = 'TQKA'
                return order.find(j) < order.find(c2)

        else:
            return self.type < other.type

def withJokers(d):
    nd = {}
    for k, i in d.items():
        if k == 'J':
            continue
        nd[k] = i + d['J']
    return nd

def checkHand2(d):
    if 'J' not in d:
        return checkHand(d)
    if len(d) == 1:
        return 7
    d = withJokers(d)
    return checkHand(d)
    

def parseLines(lines, part= 1):
    hands = []
    for line in lines:
        h, b = line.split(' ')
        if part == 1:
            hands.append(Hand(h, b))
        else:
            hands.append(Hand2(h, b))
    return hands

def changeHand(hand: str):
    d = {}
    for c in hand:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def checkFive(d):
    return len(d) == 1

def checkFour(d):
    return max(d.values()) == 4 

def checkFH(d):
    return (len(d) == 2 and max(d.values()) == 3)

def checkTOK(d):
    return len(d) == 3 and max(d.values()) == 3

def checkTP(d):
    return len(d) == 3 and max(d.values()) == 2

def checkP(d):
    return len(d) > 3 and max(d.values()) == 2

def checkHand(d):
    if checkFive(d):
        return 7
    if checkFour(d):
        return 6
    if checkFH(d):
        return 5
    if checkTOK(d):
        return 4
    if checkTP(d):
        return 3
    if checkP(d):
        return 2
    return 1


def part1():
    lines = readFile(1)
    h = parseLines(lines)
    sh = sorted(h)

    # for i , j in enumerate(sh):
    #     print(i, j)

    score = 0
    for i, j in enumerate(sh):
        score += (i+1)*j.bid
    print(score)

def part2():
    lines = readFile(1)
    h = parseLines(lines, 2)
    sh = sorted(h)

    score = 0
    for i, j in enumerate(sh):
        score += (i+1)*j.bid
    print(score)


# part1()
part2()
