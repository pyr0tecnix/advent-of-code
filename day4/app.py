# --*-- encoding: utf-8 --*--


from os import major


file = open("data/sample.txt", "r")
data = file.readlines()
file.close()


# Bingo numbers
bingoNumbers = data[0]

for key, value in enumerate(data):
    print(value)



