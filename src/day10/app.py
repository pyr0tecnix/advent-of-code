
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
            # print(caracter, lookingFor, len(chunk))
            # print("{} - {} - {}".format(key, closing[caracter], chunk))
            try:
                firstMatch = rindex(chunk[0:key], lookingFor)
                # print(lookingFor, firstMatch, chunk)
                delete_multiple_element(chunk, [key, firstMatch])
                # print(chunk)
                isCorupted(chunk)
            except (ValueError):
                # print(chunk, caracter)
                print("VE : Expected {}, but found {} instead.".format(opening[chunk[0]], caracter))
                chunk.clear()

    if chunk:
        # print(chunk)    
        print("Expected {}, but found {} instead.".format(opening[chunk[0]], opening[chunk[-1]]))
        chunk.clear()



def readChunks():
    with open('data/sample.txt') as file:
        chunks = [list(line.strip()) for line in file]


    for chunk in chunks:
        if not isIncomplete(chunk):
            isCorupted(chunk)



readChunks()
