
def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.readlines()
    file.close()
    return rawData