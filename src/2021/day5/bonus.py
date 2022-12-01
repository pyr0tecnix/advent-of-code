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


# https://newbedev.com/python-bresenham-s-line-drawing-algorithm-python-code-example
def get_line(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end
 
    >>> points1 = get_line((0, 0), (3, 4))
    >>> points2 = get_line((3, 4), (0, 0))
    >>> assert(set(points1) == set(points2))
    >>> print points1
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    >>> print points2
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
 
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
 
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
 
    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
 
    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
 
    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

mapSize = 991
map = [ [0 for i in range(mapSize)] for j in range(mapSize)]
# printMap()

for row in rawData:
    start, end = row.replace("\n", "").split(" -> ")
    start = start.split(",")
    end = end.split(",")
    start[0] = int(start[0])
    start[1] = int(start[1])
    end[0] = int(end[0])
    end[1] = int(end[1])
    print("-------")
    print(row)
    # x1 = x2
    if start[0] == end[0]:
        print("X equals : {} {}".format(start, end))
        
        for x in range(min(start[1], end[1]), max(start[1], end[1]) +1):
            map[x][start[0]] += 1
    # y1 = y2
    elif start[1] == end[1]:
        print("Y equals : {} {}".format(start, end))
        for y in range(min(start[0], end[0]), max(start[0], end[0]) +1):
            map[start[1]][y] += 1
    # break

    # Calculate function ax+b
    else:
        print("bresenham")
        points = get_line(start, end)
        for point in points:
            print(point)
            map[point[1]][point[0]] += 1
        # a = (end[1] - start[1]) / (end[0] - start[0])
        # b = ( end[0]*start[1] - start[0]*end[1]) / (end[0] - start[0])
        # print("{}x + {}".format(a, b))
        # break

# printMap()
# map[2][0] = 9
# print('------------')
# printMap()

count = 0
for row in map:
    count += row.count(0) + row.count(1)

    
print("Score : {}".format(mapSize*mapSize - count))
