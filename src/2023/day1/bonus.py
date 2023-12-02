import re

#Thanks : https://www.reddit.com/r/adventofcode/comments/1883ibu/2023_day_1_solutions/
def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    file.close()
    return rawData

data = readFile("input.txt")

litterals = [('one', 'o1e'), ('two', 't2o'), ('three', 'e3e'), ('four', 'e4e'), ('five', 'e5e'), ('six', 'e6e'), ('seven', '7e'), ('eight', 'e8e'), ('nine', 'e9e')]

def word_to_number(s):
    for k, v in litterals:
        s=s.replace(k,v)
    return s


calibration = []
for line in data:
    line = word_to_number(line)
    numerals = re.findall(r"[0-9]", line)
    if len(numerals) == 1:
        cal = [numerals[0] + numerals[0]]
    else:
        cal = [numerals[0] + numerals[-1]]
    # string to int
    calibration.append(int(cal[0]))
print(sum(calibration))