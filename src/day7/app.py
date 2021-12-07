def crabAlign():
    with open('data/sample.txt') as file:
        [initialPosition] = file.readlines()
        initialPosition = list(map(int, initialPosition.split(",")))

        minP = min(initialPosition)
        maxP = max(initialPosition)
        
        print("Bounds : {}/{}".format(minP, maxP))
        for position in initialPosition:
            print(position)


crabAlign()