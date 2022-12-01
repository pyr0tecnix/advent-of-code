def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.readlines()
    file.close()
    return rawData


data = readFile("input.txt")

elves = []
elve = []
sumOfCalories = []
for key, value in enumerate(data):
    if value == "\n":
        elves.append(elve)
        sumOfCalories.append(sum(elve))
        elve = []
    else :
        elve.append(int(value))

print("Elve carrying max calories is {} with {}".format(sumOfCalories.index(max(sumOfCalories)) + 1, max(sumOfCalories)))
print(sum(sorted(sumOfCalories, reverse=True)[:3]))

