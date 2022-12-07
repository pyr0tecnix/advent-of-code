import re

def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    # rawData = list(os.linesep.join([s for s in file.read().splitlines() if s]))
    file.close()
    return rawData

data = readFile('sample.txt')

def findIndex(data):
    # print(data,len(data), (len(data) - 1 - list(reversed(data)).index('')))
    
    return (len(data) - 1 - list(reversed(data)).index(''))


def move(crafts, q, f, t) :
    # print(crafts, crafts[t-1])

    for count in range(q):
        # Copy value

        if crafts[t-1][0] != '':
            print('Insert {} from {} to {} at index {}'.format(crafts[f-1][0], crafts[f-1], crafts[t-1], findIndex(crafts[t-1])))
            crafts[t-1].insert(t-1, crafts[f-1].pop(0))
        else:
            print('Append {} from {} to {} at index {}'.format(crafts[f-1][0], crafts[f-1], crafts[t-1], findIndex(crafts[t-1])))
            crafts[t-1][0] = crafts[f-1].pop(0)
        # Replace deplaced value
        # crafts[f-1][0] = ''
    print(crafts)
    return crafts

# Init crafts
index = 0
crafts = []

while data[index] != '':
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


# print(crafts)