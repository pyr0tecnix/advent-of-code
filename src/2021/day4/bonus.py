# --*-- encoding: utf-8 --*--

file = open("data/input.txt", "r")
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
# print(grids)


# Let's bingo
victoriousGrid = []
victoriousNumber = 0
key = 0
victoriousGridList = []
print(len(grids))
for number in bingoNumbers:
    print("current : {}".format(number))

    # Checked number in each grid
    for grid in grids:
        # print("key : {}".format(key))
        for row in range(5):
            for d in grid[row]:
                d.update((k, 1) for k, v in d.items() if k == int(number))
            # Check if we have a winner
            if getHammingWeight(getRow(grid, row)) == 5 or getHammingWeight(getColumn(grid, row)) ==  5:
                if key not in victoriousGridList:
                    victoriousGridList.append(key)

                    if len(victoriousGridList) > len(grids) - 1:
                        print("Winner is grid {} with final number {}".format(key, number))
                        victoriousGrid = grid
                        victoriousNumber = number
                        print(victoriousGrid)
                        print("*************")
                    break
        key += 1
        key = key % (len(grids))
    if len(victoriousGridList)  == len(grids):
        break

        

# Sum unchecked values
score = 0
for row in victoriousGrid:
    for d in row:
        if list(d.values())[0] == 0:
            print(list(d.keys()))
            score += list(d.keys())[0]

print("Score is {} with {} so {}".format(score, victoriousNumber, int(score)*int(victoriousNumber)))


    



