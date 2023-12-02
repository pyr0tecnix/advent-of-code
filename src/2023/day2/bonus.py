import re
from functools import reduce


def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    file.close()
    return rawData


def returnNumber(value):
    # print(value, int(re.findall("[0-9]+", value)[0]))
    return int(re.findall("[0-9]+", value)[0])

def getGameId(line):
    return returnNumber(line[0:line.find(':')])

# Return an list of 3 values r,g,b
def getTirageData(line):
    #remove Game X
    red = []
    green = []
    blue = []

    line = line[line.find(':') + 1:]
    tirages = line.split(';')
    # print(line)
    for tirage in tirages:
        #Split by color
        colorSplit = tirage.split(',')
        r = 0
        g = 0
        b = 0
        for color in colorSplit:
            if 'red' in color:
                r = returnNumber(color)
            if 'green' in color:
                g = returnNumber(color)
            if 'blue' in color:
                b = returnNumber(color)
        # print(r,g,b)
        red.append(r)
        green.append(g)
        blue.append(b)
        # print(red, green, blue)
    return [max(red), max(green), max(blue)]

def power():
    games = 0
    for line in data:
        game = getGameId(line)
        tirage = getTirageData(line)
        games += reduce((lambda x, y: x * y), tirage)

    return games


data = readFile("input.txt")

# print(getTirageData(data[0]))

print(power())


