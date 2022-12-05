import re

def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    # rawData = list(os.linesep.join([s for s in file.read().splitlines() if s]))
    file.close()
    return rawData

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


data = readFile('sample.txt')


# Init crafts
index = 0
crafts = {}
# print(crafts)
while data[index] is not '':
    # print(re.findall(r"\[([^]]*)]|\s{3}", data[index]))
    line = re.findall(r"\[([^]]*)]|\s{3}", data[index])
    index +=1
    if list(filter(None, line)):
        crafts[index] = line
    # print(index, data[index])
    # print(list(divide_chunks(data[index], 4)))

# transposed = [[row[i] for row in crafts] for i in range(len(crafts[0]))]
print(crafts)
