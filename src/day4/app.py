# --*-- encoding: utf-8 --*--

file = open("data/sample.txt", "r")
data = file.readlines()
file.close()


# Bingo numbers
bingoNumbers = data[0]
del data[0]

# Grids
grids = []

def getRow(grid, row):
    return grid[row]

def getColumn(grid, column):
    return [col[column] for col in grid]


def getHammingWeight(vector):
    weight = 0
    for key, value in enumerate(vector):
        if list(value.values())[0]:
            weight += 1
    return weight

singleGrid = []
# Bingo grid
for key, value in enumerate(data):
    # print(key, value)
    if key % 6 != 0:
        value = value.replace("\n","")
        valueList = []
        for val in value.split(" "):
            valueList.append({val:0})
        singleGrid.append(valueList)
    else:
        # print(singleGrid)
        if singleGrid:
            grids.append(singleGrid)
            singleGrid = []


print(getRow(grids[0], 1))
print(getColumn(grids[0], 1))
print(getHammingWeight(getRow(grids[0], 1)))

