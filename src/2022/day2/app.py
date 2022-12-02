def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    file.close()
    return rawData



# X rock | Y paper | Z scissors
# A rock | B paper | C scissors

values = {
    'A X': 1+3, 'A Y': 2+6, 'A Z': 3+0,
    'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6,
    'C X': 1+6, 'C Y': 2+0, 'C Z': 3+3
}

data = readFile('input.txt')

totalScore = 0
for key, round in enumerate(data):
    score = values[round]
    print('Round {} -> {}'.format(round, score))
    totalScore += score
    
print('Total score : {}'.format(totalScore))

    
    