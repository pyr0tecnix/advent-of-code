# https://github.com/littlekotok/algorithmic-coding-test/blob/master/docs/test-2.md

def readFile():
    file = open("sample.txt", "r")
    rawData = file.read().splitlines()
    # rawData = list(os.linesep.join([s for s in file.read().splitlines() if s]))
    file.close()
    return rawData

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


data = readFile()
print(data[0])

data = list(divide_chunks(data, 4))
print(data[0])


def isPayline123(attempt, symbol):
    for line in attempt[:3]:
        listLine = line.split(',')
        maxCount = max(listLine, key=listLine.count)
        if (maxCount == symbol and listLine.count(symbol) >= 3):
            return True
        else: 
            continue
    return False

def isPayline4(attempt, symbol):
    attempt[0] = attempt[0].split(',')
    attempt[1] = attempt[1].split(',')
    attempt[2] = attempt[2].split(',')

    return attempt[0][0] == symbol and attempt[0][4] == symbol and attempt[1][1] == symbol and attempt[1][3] == symbol and attempt[2][2] == symbol

def isPayline5(attempt, symbol):
    attempt[0] = attempt[0].split(',')
    attempt[1] = attempt[1].split(',')
    attempt[2] = attempt[2].split(',')

    return attempt[0][2] == symbol and attempt[1][1] == symbol and attempt[1][3] == symbol and attempt[2][0] == symbol and attempt[2][4] == symbol

total = 0
for attempt in data:
    # print(attempt)
    if(isPayline4(attempt, 'seven') or isPayline5(attempt, 'seven')):
        total += 1

print(total)