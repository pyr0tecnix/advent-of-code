
legalPairs = {'{': '}', '}': '{', '(' : ')', ')' : '(', '<' : '>', '>': '<', '[' : ']', ']' : '['}

closing = {'}':'{', ')':'(', '>':'<', ']':'['}
opening = {'{':'}', '(':')', '<':'>', '[':']'}

def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)


errors = []

def isCorupted(chunk):
    for key, caracter in enumerate(chunk):
        if caracter in closing.keys():
            # Find matching opening
            lookingFor = closing[caracter]
            # It should be just before
            # print(chunk)
            if chunk[key - 1] == lookingFor:
                # print(key, caracter, lookingFor)
                delete_multiple_element(chunk, [(key - 1), key])
                isCorupted(chunk)
            else:
                # print(chunk, key)
                print("Expected {}, but found {} instead.".format(opening[chunk[key - 1]], caracter))
                errors.append(caracter)
                chunk.clear()


def readChunks():
    with open('data/input.txt') as file:
        chunks = [list(line.strip()) for line in file]


    for chunk in chunks:
        isCorupted(chunk)

    # Score
    score = errors.count(")") * 3 + errors.count("]") * 57 + errors.count("}") * 1197 + errors.count(">") * 25137
    print(score)

readChunks()
