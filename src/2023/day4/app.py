def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    file.close()
    return rawData



data = readFile('input.txt')


# Built 3 list card | win | own
card = []
win = []
own = []
intersect = []
result = 0
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

for d in data:
    card.append(d.split(':')[0])
    d = d[d.index(':')+1:]
    # remove double blanks
    d = ' '.join(d.split())
    temp = d.split('|')
    currentWin = (temp[0].strip()).split(' ')
    currentOwn = (temp[1].strip()).split(' ')
    currentIntersect = intersection(currentWin, currentOwn)
    if len(currentIntersect) > 0:
        result += 2**(len(currentIntersect) - 1)
        # print(currentIntersect, len(currentIntersect),  2**(len(currentIntersect) - 1))

        intersect.append(currentIntersect)

    win.append(currentWin)
    own.append(currentOwn)
print(result)
