def printMap(m):
    for row in m:
        print(row)

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



with open('data/sample.txt') as file:
    octopusMap = [list(map(int, line.strip())) for line in file]

    printMap(octopusMap)
    printValues([[3,4]], octopusMap)
    printValues(findAdjacentIndex(3, 4), octopusMap)



