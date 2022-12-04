def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    file.close()
    return rawData



data = readFile('input.txt')


lowerTranscription = ['', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperTranscription = ['', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y', 'Z']
backpacks = []

# foo = 'abcABC'
# print([ord(char) - 96 for char in foo] if foo.islower() else [ord(char) - 65 for char in foo])

for key, value in enumerate(data):
    part1 = value[:len(value)//2]
    part2 = value[len(value)//2:]
    # backpacks.append([part1, part2, set(part1).intersection(part2)]) # return a set object
    backpacks.append([part1, part2, list(set(part1) & set(part2))]) # return a list

totalValue = 0
for b in backpacks:
    commonLetter = b[2][0]
    value = lowerTranscription.index(commonLetter) if commonLetter.islower() else upperTranscription.index(commonLetter) + 26
    print('{} - {}'.format(commonLetter, value))
    totalValue += value

print('total : {}'.format(totalValue))