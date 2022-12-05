import re

def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    # rawData = list(os.linesep.join([s for s in file.read().splitlines() if s]))
    file.close()
    return rawData

data = readFile('sample.txt')

def move(crafts, q, f, t):
    print('---------', q, f, t)
    print(crafts)
    for i in range(1, q+1):
        # print(f, t, crafts[f-1], crafts[t-1])
        index = 0 if crafts[t-1] is not '' else 1

        crafts[t-1][index] = crafts[f-1][0]
        crafts[f-1][0] = ''
    return crafts

# Init crafts
index = 0
crafts = []

while data[index] is not '':
    line = re.findall(r"\[([^]]*)]|\s{3}", data[index])
    index +=1
    if list(filter(None, line)):
        crafts.append(line)


# Transpose
crafts = list(map(list, zip(*crafts)))

# Get instructions
instructions = []
for line in data:
    _move = re.findall(r"move (\d+)", line)
    _from = re.findall(r"from (\d+)", line)
    _to = re.findall(r"to (\d+)", line)
    if _move:
        crafts = move(crafts, int(_move[0]), int(_from[0]), int(_to[0]))
        # instructions.append([int(_move[0]), int(_from[0]), int(_to[0])])

print(crafts)