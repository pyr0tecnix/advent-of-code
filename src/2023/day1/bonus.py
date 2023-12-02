import re


def readFile(filename):
    file = open("data/{}".format(filename), "r")
    rawData = file.read().splitlines()
    file.close()
    return rawData

data = readFile("sample_bonus.txt")

litterals = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')]

def recursive_replace(s):
    if(s.isnumeric()):
        return s
    index = next(i for i, j in enumerate(s) if j not in ['1','2','3','4','5','6','7','8','9'])
    # print(s, index, s[index:], s[index:].startswith('nine'))
    if index >=0 :
        if s[index:].startswith('one'):
            s = s.replace('one', '1', 1)
            recursive_replace(s)
        if s[index:].startswith('two'):
            s = s.replace('two', '2', 1)
            recursive_replace(s)
        if s[index:].startswith('three'):
            s = s.replace('three', '3', 1)
            recursive_replace(s)
        if s[index:].startswith('four'):
            s = s.replace('four', '4', 1)
            recursive_replace(s)
        if s[index:].startswith('five'):
            s = s.replace('five', '5', 1)
            recursive_replace(s)
        if s[index:].startswith('six'):
            s = s.replace('six', '6', 1)
            recursive_replace(s)
        if s[index:].startswith('seven'):
            s = s.replace('seven', '7', 1)
            recursive_replace(s)
        if s[index:].startswith('eight'):
            s = s.replace('eight', '8', 1)
            recursive_replace(s)
        if s[index:].startswith('nine'):
            s = s.replace('nine', '9', 1)
            recursive_replace(s)
    return s

calibration = []
for line in data:
    # Transcrypt litteral numbers
    # for key, value in litterals:
    #     line = line.replace(key, value)
    s = recursive_replace(recursive_replace(line))
    print(s)
#     numerals = re.findall(r"[0-9]", line)
#     if len(numerals) == 1:
#         cal = [numerals[0] + numerals[0]]
#     else:
#         cal = [numerals[0] + numerals[-1]]
#     # string to int
#     calibration.append(int(cal[0]))
# print((calibration))