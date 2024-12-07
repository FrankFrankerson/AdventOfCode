import math

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()
    
def parseLines(lines):
    data = {}
    for line in lines:
        line = line.strip('\n')
        total, nums = line.split(': ')
        if total not in data:
            data[total] = nums.split(' ')
        else:
            print('Duplicate total')
    return data

def numberToBase(n, b):
    if n == 0:
        return '0'
    digits = ''
    while n:
        digits+=str(int(n % b))
        n //= b
    return digits[::-1]

def checkFormula(nums, s, operators):
    t = int(nums[0])
    for i, n in enumerate(nums[1:]):
        o = operators[int(s[i])]
        if o == '||':
            o = ''
        ev = str(t) + o + n
        t = eval(ev)
    return t

def checkTotal(total: str, nums: list[str], operators: list[str], base = 2):
    places = len(nums) - 1
    evTotal = 0
    c = -1

    while True: 
        c += 1
        s = numberToBase(c, base)
        s = s.zfill(places)
        evTotal = checkFormula(nums, s, operators)
        if evTotal == int(total):
            return int(total)
        if s == str(base)*places:
            break
    return 0


def part1():
    lines = readFile(1)
    data = parseLines(lines)

    operators = ['+', '*']
    s = 0
    for t, nums in data.items():
        s += checkTotal(t, nums, operators)
    print(s)

def part2():
    lines = readFile(1)
    data = parseLines(lines)

    operators = ['+', '*', '||']
    s = 0
    c = 1
    for t, nums in data.items():
        print(f'{c/len(data):.2}')
        s += checkTotal(t, nums, operators, base=3)
        c+=1
    print(s)

# part1()
part2()