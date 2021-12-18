
legalPairs = {'{': '}', '}': '{', '(' : ')', ')' : '(', '<' : '>', '>': '<', '[' : ']', ']' : '['}

closing = {'}':'{', ')':'(', '>':'<', ']':'['}
opening = {'{':'}', '(':')', '<':'>', '[':']'}

def rindex(lst, value):
    caractList = lst
    # print("Rindex list : {}".format(len(lst)))
    caractList.reverse()
    i = caractList.index(value)
    caractList.reverse()
    return len(caractList) - i - 1

def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)


def isIncomplete(chunk):
    return len(chunk) % 2 != 0

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
                chunk.clear()


def readChunks():
    with open('data/sample.txt') as file:
        chunks = [list(line.strip()) for line in file]


    for chunk in chunks:
        isCorupted(chunk)



readChunks()
