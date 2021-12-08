def moveToPosition(crabs, position):
    crabLine = []
    for key, crab in enumerate(crabs):
        crabLine.append(abs(crab - position))

    return sum(crabLine)


def decode7segment():
    with open('data/sample.txt') as file:
        data = file.readlines()
        signals, output = data.split("|")
        print(output)


decode7segment()