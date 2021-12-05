# --*-- encoding: utf-8 --*--

file = open("data/input.txt", "r")
rawData = file.readlines()
file.close()

# Utilities
def getRow(grid, row):
    return grid[row]


def printMap():
    for row in map:
        print(row)


instructions = []
map = [ [0 for i in range(991)] for j in range(991)]
# printMap()

for row in rawData:
    start, end = row.replace("\n", "").split(" -> ")
    start = start.split(",")
    end = end.split(",")
    start[0] = int(start[0])
    start[1] = int(start[1])
    end[0] = int(end[0])
    end[1] = int(end[1])

    print(row)
    # x1 = x2
    if start[0] == end[0]:
        print("X equals : {} {}".format(start, end))
        
        for x in range(min(start[1], end[1]), max(start[1], end[1]) +1):
            map[x][start[0]] += 1
    # y1 = y2
    if start[1] == end[1]:
        print("Y equals : {} {}".format(start, end))
        for y in range(min(start[0], end[0]), max(start[0], end[0]) +1):
            map[start[1]][y] += 1
    # break
# printMap()

count = 0
for row in map:
    count += row.count(0) + row.count(1)

    
print("Score : {}".format(982081 - count))
