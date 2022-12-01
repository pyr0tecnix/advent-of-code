def moveToPosition(crabs, position):
    crabLine = []
    for key, crab in enumerate(crabs):
        crabLine.append(abs(crab - position))

    return sum(crabLine)


def crabAlign():
    with open('data/input.txt') as file:
        [initialPosition] = file.readlines()
        initialPosition = list(map(int, initialPosition.split(",")))

        minP = min(initialPosition)
        maxP = max(initialPosition)
        print("Bounds : {}/{}".format(minP, maxP))
        # printMap(hypothesis)

        positions = []
        for i in range(maxP):
           positions.append(moveToPosition(initialPosition, i))
        #    print(positions)

        print("Minimum value {}".format(min(positions)))


crabAlign()