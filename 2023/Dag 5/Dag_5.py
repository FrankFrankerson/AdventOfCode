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
    tag = ''
    almanac = {}
    while lines:
        line = lines.pop(0)
        line = line.strip("\n")
        if not line:
            continue
        if ':' in line:
            tag, content = line.split(':')
            if tag == 'seeds':
                seedsStr = content.split(' ')[1:]
                seeds = []
                for i in seedsStr:
                    seeds.append(str(i))
            else:
                tag = tag.strip(' map')
                # beg, _, end = tag.split('-')
                almanac[tag] = {}
        else:
            dest, src, rang = line.split(' ')
            for i in range(int(rang)):
                almanac[tag][int(src)+i] = int(dest) + i
                # almanac[tag][int(dest)+i] = int(src) + i    
    return almanac, seeds
# tags 'seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location'


def part1():
    lines = loadInput()
    almanac, seeds = parseLines(lines)
    tags = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

    minLoc = None
    for seed in seeds:
        prev = int(seed)
        for tag in tags:
            if prev in almanac[tag]:
                prev = almanac[tag][prev]
        if minLoc:
            minLoc = min(minLoc, prev)
        else:
            minLoc = prev
    print(minLoc)
part1()