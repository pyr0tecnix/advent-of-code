
legalPairs = {'{': '}', '}': '{', '(' : ')', ')' : '(', '<' : '>', '>': '<', '[' : ']', ']' : '['}

def isIncomplete(chunk):
    return len(chunk) % 2 != 0

def isCorupted(chunk):
    delimiter = int(len(chunk) / 2)
    print(delimiter)
    firstHalf = chunk[:delimiter]
    secondHalf = chunk[delimiter:]
    print("{} is {} and {}".format(chunk, firstHalf, secondHalf))

def readChunks():
    with open('data/sample.txt') as file:
        chunks = [line.strip() for line in file]
        

    for chunk in chunks:
        if not isIncomplete(chunk):
            isCorupted(chunk)




readChunks()

print(legalPairs['('])