# --*-- encoding: utf-8 --*--


count = 0


file = open("data/input.txt")
data = file.readlines()
file.close()

windowed = []

for (index, value) in enumerate(data):
    if (index > 1) and (index < len(data)):
        current, previous, antePrevious = value, data[index - 1], data[index - 2]
        print(antePrevious, previous,current, int(current) + int(previous) + int(antePrevious))
        windowed.append(int(current) + int(previous) + int(antePrevious))
    # if(index > 20):
    #     break


for (index, value) in enumerate(windowed):
    if (index < len(data)):
        current, previous = value, windowed[index - 1]
        print(previous, current, current > previous)
        if(int(current) > int(previous)):
            count +=1

print(count)