import re
from functools import reduce

def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    file.close()
    return rawData


data = readFile('sample.txt')

def isAdjacent(start, end, dataIndex):

    if dataIndex == 0:
        # First line
        print(data[dataIndex][end + 1], data[dataIndex + 1])
        if data[dataIndex][end + 1] not in [0,1,2,3,4,5,6,7,8,9,'.'] and data[dataIndex + 1] not in [0,1,2,3,4,5,6,7,8,9,'.']:
            return True
        return False
    elif dataIndex == 9:
        # Last line
        return True
    else:
        # Middle
        return True

print(data)

# Find all numbers in input
numbers = [re.findall(r'\d+', i) for i in data]

# Reduce list
numbers = reduce((lambda x, y: x + y), numbers)

# Sum list
total = reduce((lambda x, y: int(x)+ int(y)), numbers)

dataBound = [0, len(data) - 1]
# print(dataBound)

# Loop through numbers
for n in numbers:
    res = [i for i in data if n in i]
    indexOfList = data.index(res[0])
    # print(n, res, len(n), indexOfList)
    if not isAdjacent(data[indexOfList].find(n), len(n), indexOfList):
        print('Exclude', n)
        total -= int(n)


print(total)


