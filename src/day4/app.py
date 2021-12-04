# --*-- encoding: utf-8 --*--


from os import major


file = open("data/sample.txt", "r")
data = file.readlines()
file.close()


# Bingo numbers
bingoNumbers = data[0]
del data[0]

# Grids
grids = []

singleGrid = []
# Bingo grid
for key, value in enumerate(data):
    # print(key, value)
    if key % 6 != 0:
        singleGrid.append(value.replace("\n",""))
    else:
        print(singleGrid)
        grids.append(singleGrid)
        singleGrid = []


# print(grids)


