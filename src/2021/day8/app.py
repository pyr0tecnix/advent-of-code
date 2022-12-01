

def decode7segment():
    with open('data/input.txt') as file:
        data = file.readlines()
        signals = [line.split("|")[0].strip() for line in data]
        outputs = [line.split("|")[1].strip() for line in data]

    # By obvious I mean 1, 4, 7 and 8
    totalObvious = 0
    for output in outputs:
        outList = output.split(" ")
        print(outList)
        totalObvious+= sum(map(lambda x: len(x) == 2, outList)) + sum(map(lambda x: len(x) == 3, outList)) + sum(map(lambda x: len(x) == 4, outList)) + sum(map(lambda x: len(x) == 7, outList))

    print(totalObvious)
decode7segment()
