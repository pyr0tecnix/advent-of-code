import os

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


data = readFile('input.txt')
data = list(filter(None, data)) # Remove empty element coming from empty lines

# print(data)

# data = list(divide_chunks(data, 2))
processedData = []

subsetCount = 0
for key, value in enumerate(data):
    # print(value.split(','))
    # pass
    range1Start = int(value.split(',')[0].split('-')[0])
    range1End = int(value.split(',')[0].split('-')[1]) + 1
    range2Start = int(value.split(',')[1].split('-')[0])
    range2End = int(value.split(',')[1].split('-')[1]) + 1

    range1, range2 = range(range1Start, range1End),range(range2Start, range2End)
    processedData.append([value, range1, range2])
    
    if set(range1).issubset(set(range2)) or set(range2).issubset(set(range1)):
        subsetCount+=1

print(subsetCount)