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

def checkIncreasing(report):
    for i, num in enumerate(report):
        if i == 0:
            continue
        elif num < report[i-1] + 1 or num > report[i-1] + 3:
            return False
    return True

def checkDecreasing(report):
    for i , num in enumerate(report):
        if i == 0:
            continue
        elif num > report[i-1] - 1 or num < report[i-1] - 3:
            return False
    return True

def checkIncreasingTolerate(report):
    tolerate = True
    prev = report.pop(0)
    while report != []:
        curr = report.pop(0)
        if curr < prev + 1 or curr > prev + 3:
            if tolerate:
                tolerate = False
                continue
            else:
                return False
        prev = curr
    return True

def checkDecreasingTolerate(report):
    tolerate = True
    prev = report.pop(0)
    while report != []:
        curr = report.pop(0)
        if curr > prev - 1 or curr < prev - 3:
            if tolerate:
                tolerate = False
                continue
            else:
                return False
        prev = curr
    return True

def calcAnswer(reports):
    t = 0
    for i, report in enumerate(reports):
        if checkIncreasing(report.copy()):
            t += 1
            print(f'{i} Inc', report)
        elif checkDecreasing(report.copy()):
            t += 1
            print(f'{i} Dec', report)

    return t

def checkPermutations(report):
    for i in range(len(report)):
        newReport = report.copy()
        newReport.pop(i)
        if checkDecreasing(newReport) or checkIncreasing(newReport):
            return True, i
    return False, 0


def calcAnswer2(reports):
    t = 0
    for i, report in enumerate(reports):
        if checkIncreasing(report):
            t += 1
            print(f'{i} Inc', report)
        elif checkDecreasing(report.copy()):
            t += 1
            print(f'{i} Dec', report)
        else:
            b, j = checkPermutations(report)
            if b:
                t += 1
                print(f'{i} perm:', j)
    return t

def part1():
    # lines = loadExample()
    lines = loadInput()
    reports = parseLines(lines)
    print(calcAnswer(reports))

def part2():
    # lines = loadExample()
    lines = loadInput()
    reports = parseLines(lines)
    print(calcAnswer2(reports))

# part1()
part2()