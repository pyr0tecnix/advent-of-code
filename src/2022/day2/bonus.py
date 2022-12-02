def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    file.close()
    return rawData


# X lose | Y draw | Z win
transcription = {
    'A X': 'A Z', 'A Y': 'A X', 'A Z': 'A Y',
    'B X': 'B X', 'B Y': 'B Y', 'B Z': 'B Z',
    'C X': 'C Y', 'C Y': 'C Z', 'C Z': 'C X'
}

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
    decode = transcription[round]
    score = values[decode]
    print('Round {} - {} -> {}'.format(round, decode, score))
    totalScore += score
    
print('Total score : {}'.format(totalScore))

    
    