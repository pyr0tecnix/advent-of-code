# --*-- encoding: utf-8 --*--


file = open("data/input.txt")
data = file.readlines()
file.close()

depth = 0;
horizontal = 0;

for (index, instruction) in enumerate(data):

    singleInstruction = instruction.split(' ')
    print(singleInstruction)
    if "forward" in singleInstruction[0]:
        horizontal += int(singleInstruction[1])
    elif "down" in singleInstruction[0]:
        depth += int(singleInstruction[1])
    elif "up" in singleInstruction[0]:
        depth -= int(singleInstruction[1])

print(horizontal, depth, horizontal*depth)



