def moveToPosition(crabs, position):
    crabLine = []
    for key, crab in enumerate(crabs):
        cost = ((abs(crab - position)*(abs(crab - position)+ 1)/2 ));
        crabLine.append(abs(cost))

    return sum(crabLine)



def crabAlign():
    with open('data/input.txt') as file:
        [initialPosition] = file.readlines()
        initialPosition = list(map(int, initialPosition.split(",")))

        minP = min(initialPosition)
        maxP = max(initialPosition)
        print("Bounds : {}/{}".format(minP, maxP))


        positions = []
        for i in range(maxP):
           positions.append(moveToPosition(initialPosition, i))
        print(positions)

        print("Minimum value {}".format(min(positions)))


crabAlign()