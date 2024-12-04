def readFile(inp):
    if inp:
        fileName = 'input.txt'
    else:
        fileName ='ex_input.txt'
    with open(fileName, 'r') as f:
        return f.readlines()
