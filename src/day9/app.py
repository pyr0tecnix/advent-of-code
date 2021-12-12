# Utilities
def getRow(grid, row):
    return grid[row]

def getColumn(grid, column):
    return [col[column] for col in grid]

def printMap(map):
    for row in map:
        print(row)
    print("")

""" Add 9 to border to make comparison easir """
def formatHeightMap(heightmap):
    newMap = []
    for line in heightmap:
        line = list(map(int, line))

        # Append 9 at the begining and the end
        line.insert(0,9)
        line.append(9)
        newMap.append(line)
    # Append a line of 9 at the begining and the end
    newMap.insert(0, [9 for i in range(len(newMap[0]))])
    newMap.append([9 for i in range(len(newMap[0]))])

    return newMap


def getCommonLocal(rowMap, colMap):
    total = 0
    flowMap = [ [None for i in range(len(rowMap[0]))] for j in range(len(rowMap))]
    for i in range(len(rowMap)):
        for j in range(len(rowMap[0])):
            # print(i,j)
            if rowMap[i][j] == colMap[i][j]:
                flowMap[i][j] = rowMap[i][j]
                if rowMap[i][j] != None:
                    total += flowMap[i][j] + 1
                    print("Common min")
    print("Result : {}".format(total))
    return flowMap
    

def readLavaFlow():
    with open('data/input.txt') as file:
        heightmap = file.read().splitlines()
        heightmap = formatHeightMap(heightmap)
        # # Init flowMap (result)
        flowRowMap = [ [None for i in range(len(heightmap[0]))] for j in range(len(heightmap))]
        flowColumnMap = [ [None for i in range(len(heightmap[0]))] for j in range(len(heightmap))]

        # printMap(heightmap)

        # Read lines
        lineIndex = 0
        for line in heightmap:
            # print(line)
            for index, flow in enumerate(line):
                if (index < (len(line)) - 1):
                    previous, current, next = line[index - 1], line[index], line[index + 1] 
                    # print(previous, current, next)   

                    # Is local minimum
                    if current < previous and current < next:
                        # print("Flow found with {} ! {} {}".format(current, index, key))
                        flowRowMap[lineIndex][index] = current
            lineIndex += 1


        # Read columns
        for key in range(len(heightmap[0])):
            column = getColumn(heightmap, key)
            # print(column)
            for index, flow in enumerate(column):
                if (index < (len(column)) - 1):
                    previous, current, next = column[index - 1], column[index], column[index + 1] 
                    # print(previous, current, next)    

                    # Is local minimum
                    if current < previous and current < next:
                        # print("Flow found with {} ! {} {}".format(current, index, key))
                        flowColumnMap[index][key] = current

    printMap(flowRowMap)
    printMap(flowColumnMap)
    flowMap = getCommonLocal(flowRowMap, flowColumnMap)
    # printMap(flowMap)
readLavaFlow()