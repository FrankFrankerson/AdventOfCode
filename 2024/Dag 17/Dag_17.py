import collections

def readFile(file=0):
    fileName = 'input.txt' if file else 'ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()

def parseLines(lines):
    for i, line in enumerate(lines):
        line = line.strip('\n')
        for j, letter in enumerate(line):
            pass

class Computer:

    def __init__(self, value_A, value_B, value_C):
        self.a = value_A
        self.b = value_B
        self.c = value_C
        self.output = []
        self.pointer = 0
        self.programMap = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }
    
    def runProgram(self, program):
        # print('program:',program)
        program = program.split(',')
        program = list(map(int, program))
        
        while self.pointer < len(program):
            # print(self.a)
            command = program[self.pointer]
            value = program[self.pointer+1]
            self.programMap[command](value)
            # print(f'command: {command}, value: {value}')
        # self.printOutput()

    def reset(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.output = []
        self.pointer = 0

    def runCopy(self, program, tryA = 1):
        program = program.split(',')
        program = list(map(int, program))
        # tryA = 1
        equalScore = 0
        tryPlus = 1
        while self.output != program:
            if len(self.output) > 0:
                score = 0
                for i, j in enumerate(reversed(self.output)):
                    if j == list(reversed(program))[i]:
                        score += 1
                if score > equalScore:
                    equalScore = score
                    tryA*=8
                    print(f'Score: {score} A: {tryA} {self.output}')
                else:
                    tryA += 1
            else:
                tryA += 1
            self.reset()
            self.a = tryA
            breakLoop = False

            while self.pointer < len(program) and not breakLoop:
                command = program[self.pointer]
                value = program[self.pointer+1]
                self.programMap[command](value)
        print(tryA)
        self.printOutput()

    def printOutput(self):
        st = ''
        for i in self.output:
            st += f',{str(i)}'
        print('output', st[1:])
        print('Register A:', self.a)
        print('Register B:', self.b)
        print('Register C:', self.c)

    def combo(self, v):
        if v < 4:
            return v
        if v == 4:
            return self.a
        if v == 5:
            return self.b
        if v == 6:
            return self.c
        if v == 7:
            print('Error, this is reserved')

    def adv(self, v):
        self.a = self.a//(2**self.combo(v))
        self.pointer += 2

    def inv_adv(self, v):
        self.a = self.a * (2**self.combo(v))
        self.pointer += 2

    def bxl(self, v):
        self.b = self.b ^ v
        self.pointer += 2

    def inv_bxl(self,v):
        self.b = self.b ^ v
        self.pointer += 2
            
    def bst(self, v):
        self.b = self.combo(v)%8
        self.pointer += 2

    # def inv_bst(self, v):
    #     self.b 

    def jnz(self, v):
        if self.a == 0:
            self.pointer += 2
        else:
            self.pointer = v

    def bxc(self, v):
        self.b = self.b ^ self.c
        self.pointer += 2
    
    def out(self, v):
        self.output.append(self.combo(v)%8)
        self.pointer += 2
    
    def bdv(self, v):
        self.b = self.a//(2**self.combo(v))
        self.pointer += 2
    
    def cdv(self, v):
        self.c = self.a//(2**self.combo(v))
        self.pointer += 2

# comp = Computer(812125953, 0, 0)
comp = Computer(0, 0, 0)
# comp.runProgram('2,4,1,5,7,5,1,6,0,3,4,3,5,5,3,0')
comp.runCopy('2,4,1,5,7,5,1,6,0,3,4,3,5,5,3,0', 1)
# program = '2,4,1,5,7,5,1,6,0,3,4,3,5,5,3,0'
# comp = Computer(3, 0, 0)
# comp.runProgram(program)
# comp.printOutput()
# for i in range(8):
#     comp = Computer(0,0,0)
#     j = 0
#     while not comp.output or comp.output[-1] != i and j < 1000:
#         comp.reset()
#         j += 1
#         comp.a = j
#         comp.runProgram(program)
#     print(i, j)

# comp = Computer(729, 0, 0)
# comp.runProgram('0,1,5,4,3,0')

# comp = Computer(0, 0, 9)
# comp.runProgram('2,6')

# comp = Computer(10, 0, 0)
# comp.runProgram('5,0,5,1,5,4')

# comp = Computer(2024, 0, 0)
# comp.runProgram('0,1,5,4,3,0')

# comp = Computer(0, 29, 0)
# comp.runProgram('1,7')

