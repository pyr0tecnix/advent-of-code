def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    file.close()
    return rawData

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

data = readFile('input.txt')


lowerTranscription = ['', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperTranscription = ['', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y', 'Z']
backpacks = []

# print(data)
groupedElves = list(divide_chunks(data, 3))
for key, value in enumerate(groupedElves):
    # backpacks.append([part1, part2, set(part1).intersection(part2)]) # return a set object
    backpacks.append([value, list(set(value[0]) & set(value[1]) & set(value[2]))]) # return a list

# print(backpacks)

totalValue = 0
for b in backpacks:
    commonLetter = b[1][0]
    value = lowerTranscription.index(commonLetter) if commonLetter.islower() else upperTranscription.index(commonLetter) + 26
    print('{} - {}'.format(commonLetter, value))
    totalValue += value

print('total : {}'.format(totalValue))