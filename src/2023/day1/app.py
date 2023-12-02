import re


def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    file.close()
    return rawData

data = readFile("sample.txt")

calibration = []
for line in data:
    numerals = re.findall(r"[0-9]", line)
    if len(numerals) == 1:
        cal = [numerals[0] + numerals[0]]
    else:
        cal = [numerals[0] + numerals[-1]]
    # string to int
    calibration.append(int(cal[0]))
print(sum(calibration))