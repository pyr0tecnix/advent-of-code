# --*-- encoding: utf-8 --*--


count = 0


file = open("data/input.txt")
data = file.readlines()
file.close()


for (index, value) in enumerate(data):
    if (index > 0) and (index < len(data)):
        current, previous = value, data[index - 1]
        # print(previous, current, current > previous)
        if(int(current) >= int(previous)):
            count +=1

print(count)




