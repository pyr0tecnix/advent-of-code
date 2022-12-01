def printMap(m):
    for row in m:
        print(row)
    print("\n")

def printValues(indexes, m):
    v = [] 
    for index in indexes:
        v.append(m[index[0]][index[1]])
    print(v)

def findAdjacentIndex(y, x):
    
    #Top-left
    if y == 0 and x == 0:
        return [[1, 0], [0, 1], [1, 1]]

    #Bottom-left
    elif y == 9 and x == 0:
        return [[8, 0], [9, 1], [9, 2]]

    #Top-right
    elif y == 0 and x == 9:
        return [[0, 8], [1, 9], [1, 8]]

    #Bottom-right
    elif y == 9 and x == 9:
        return [[8, 9], [9, 8], [8, 8]]

    #Top border
    elif y == 0 and x != 0 and x != 9:
        return [[y, x-1], [y+1, x-1], [y+1,x], [y+1, x+1], [y, x+1]]

    #Bottom border
    elif y == 9 and x != 0 and x != 9:
        return [[y, x-1],  [y-1, x-1], [y-1, x], [y-1, x+1], [y, x+1]]

    #Left border
    elif x == 0 and y != 0 and y != 9:
        return [[y-1, x], [y-1, x+1], [y, x+1], [y+1, x+1], [y+1, x]]

    #Right-border
    elif x == 9 and y != 0 and y !=9:  
        return [[y-1, x], [y-1, x-1], [y, x-1], [y+1, x-1], [y+1, x]]

    #Other
    else:
        return [[y-1, x-1], [y, x-1], [y+1, x-1], [y+1, x], [y+1, x+1], [y, x+1], [y-1, x+1], [y-1, x]]


def getReadyToFlash(m):
    flash = [[[key, i] for i in range(len(line)) if line[i] > 9] for key,line in enumerate(m)]
    return [item for subL in flash for item in subL]


def performFlash(octopusMap):
    octopusReadyToFlash = getReadyToFlash(octopusMap)
    if octopusReadyToFlash:
        for octopus in octopusReadyToFlash:
            adjacent = findAdjacentIndex(octopus[0], octopus[1])
            #Increase adjacent
            for point in adjacent:
                if octopusMap[point[0]][point[1]] != 0: # Flash only once per step
                    octopusMap[point[0]][point[1]] += 1

            #After flash point is reset to 0
            octopusMap[octopus[0]][octopus[1]] = 0

        performFlash(octopusMap)


with open('data/input.txt') as file:
    octopusMap = [list(map(int, line.strip())) for line in file]
    flashCounter = 0
    # printMap(octopusMap)
    # printValues([[3,4]], octopusMap)
    # printValues(findAdjacentIndex(3, 4), octopusMap)
    for step in range(1, 1001):
        # print(step)
        # Increment
        octopusMap = [[element + 1 for element in line] for line in octopusMap]
        # printMap(octopusMap)
        performFlash(octopusMap)
        flashCounter += sum([line.count(0) for line in octopusMap])
    printMap(octopusMap)
    print(flashCounter)


