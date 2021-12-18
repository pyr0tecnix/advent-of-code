
legalPairs = {'{': '}', '}': '{', '(' : ')', ')' : '(', '<' : '>', '>': '<', '[' : ']', ']' : '['}

closing = {'}':'{', ')':'(', '>':'<', ']':'['}
opening = {'{':'}', '(':')', '<':'>', '[':']'}

def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)


errors = []

def isCorupted(index, chunk):
    for key, caracter in enumerate(chunk):
        if caracter in closing.keys():
            # Find matching opening
            lookingFor = closing[caracter]
            # It should be just before
            # print(chunk)
            if chunk[key - 1] == lookingFor:
                # print(key, caracter, lookingFor)
                delete_multiple_element(chunk, [(key - 1), key])
                isCorupted(index, chunk)
            else:
                # print(chunk, key)
                # print("Expected {}, but found {} instead.".format(opening[chunk[key - 1]], caracter))
                errors.append(index)
                chunk.clear()

missing = []
def addMissingCaracter(chunk):
    for key, caracter in enumerate(chunk):
        if caracter in opening.keys():
            # print(chunk)
            # print(missing)
            lookingFor = opening[caracter]
            # print("0", key)
            if key == 0:
                missing.append(opening[caracter])
                # print("prout", key, caracter, opening[caracter])
                # addMissingCaracter(chunk)
            elif chunk[key - 1] == lookingFor:
                # print("1")
                # print(key, caracter, lookingFor)
                delete_multiple_element(chunk, [(key - 1), key])
                addMissingCaracter(chunk)
            else:
                missing.append(opening[chunk[key - 1]])


scores = []
def readChunks():
    with open('data/input.txt') as file:
        chunks = [list(line.strip()) for line in file]

        for index, chunk in enumerate(chunks):
            isCorupted(index, chunk)

    with open('data/input.txt') as file:
        chunks = [list(line.strip()) for line in file]

        # Incomplete
        for index, chunk in enumerate(chunks):
            if index in errors:
                continue
            chunk.reverse()
            addMissingCaracter(chunk)
            
            # Scoring
            score = 0
            for c in chunk:
                score *= 5
                if opening[c] == ")":
                    score += 1
                if opening[c] == "]":
                    score += 2
                if opening[c] == "}":
                    score += 3
                if opening[c] == ">":
                    score += 4
            scores.append(score)

        scores.sort()
        mid = len(scores) // 2
        med = (scores[mid] + scores[~mid]) / 2
        print(scores, med)

readChunks()
