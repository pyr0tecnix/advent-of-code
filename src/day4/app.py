# --*-- encoding: utf-8 --*--

file = open("data/sample.txt", "r")
data = file.readlines()
file.close()

# Utilities
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

# Bingo numbers
bingoNumbers = (data[0]).split(",")
del data[0]

# Grids
grids = []

singleGrid = []

# Build Bingo grid
for key, value in enumerate(data):
    # print(key, value)
    if key % 6 != 0:
        value = value.replace("\n","").strip().replace("  ", " ") # use strip to handle single digit number
        valueList = []
        for val in value.split(" "):
            valueList.append({int(val):0})
        singleGrid.append(valueList)
    else:
        # print(singleGrid)
        if singleGrid:
            grids.append(singleGrid)
            singleGrid = []


# print(getRow(grids[0], 0))
# print(getColumn(grids[0], 0))
# print(getHammingWeight(getRow(grids[0], 0)))



# Let's bingo

for number in bingoNumbers:
    print(number)
    # Checked number in each grid
    for grid in grids:
        for row in range(5):
            # print(grid[row])
            if any (int(number) in d for d in grid[row]):
                print(grid[row])
