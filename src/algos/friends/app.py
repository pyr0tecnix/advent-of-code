#https://github.com/littlekotok/algorithmic-coding-test/blob/master/docs/test-1.md

def readFile():
    file = open("sample.txt", "r")
    rawData = file.read().splitlines()
    # rawData = list(os.linesep.join([s for s in file.read().splitlines() if s]))
    file.close()
    return rawData


def splitRelation(sentence, separator):
    # print(sentence)
    return sentence.split(separator)

data = readFile()
# print(data[0])

# Build friendship tree
relationTree = {}

# Add personal relation
relationTree['me'] = [[s.strip() for s in splitRelation(data[-3], 'am friends with')][1]]

for sentence in data[:-3]:
    named = [s.strip() for s in splitRelation(sentence, 'is friends with')]

    #First
    if named[0] in relationTree:
        relationTree[named[0]].append(named[1])
    else:
        relationTree[named[0]] = [named[1]]
    #Apply reciprocity
    if named[1] in relationTree:
        relationTree[named[1]].append(named[0])
    else:
        relationTree[named[1]] = [named[0]]

# relationTree['me'] = [s.strip() for s in splitRelation(data[-3], 'am friends with')][1]

print(relationTree)



# Question
question = data[-1].split(' ')[1]
if question in relationTree['me']:
    print('Yes maam')
else:
    print('Nope')

