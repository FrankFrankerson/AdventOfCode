if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        lines = f.readlines()

def isNum(s):
    if s in '0123456789':
        return True
    else:
        return False
    
def checkNum(s: str):
    nums = '0123456789'
    for i in nums:
        if i in s:
            return True, i
    return False, -1

def changeTextToNum(s):
    if s == 'one':
        return '1'
    elif s == 'two':
        return '2'
    elif s == 'three':
        return '3'
    elif s == 'four':
        return '4'
    elif s == 'five':
        return '5'
    elif s == 'six':
        return '6'
    elif s == 'seven':
        return '7'
    elif s == 'eight':
        return '8'
    elif s == 'nine':
        return '9'
    else:
        return '0'


def checkText(s: str):
    text = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
    for i in text:
        if i in s:
            return True, changeTextToNum(i)
    return False, -1

    

def breakDownLine(line: str, reverse = False):
    s = ''
    for i in line:
        if reverse:
            s = i + s
        else:
            s += i

        b, v = checkNum(s)
        if b:
            return v
        
        b, v = checkText(s)
        if b:
            return v
    
         

def findNums(line):
    numb1 = breakDownLine(line)
    rLine = reversed(line)
    numb2 = breakDownLine(rLine, reverse=True)
    print(numb1, numb2)
    return int(numb1+numb2)

def findCal(lines):
    sum = 0
    for line in lines:
        sum += findNums(line)
    print(sum)

findCal(lines)