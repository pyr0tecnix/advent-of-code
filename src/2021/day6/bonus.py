# --*-- encoding: utf-8 --*--

file = open("data/input.txt", "r")
initial = file.readlines()
file.close()

lanternfish = []
# Utilities

def lfish(days):
    with open('data/input.txt') as file:
        lines = file.readlines()
    lines = [line.rstrip().split(",") for line in lines][0]
    fishes = [0]*9
    for i in [int(x) for x in lines]: #the initial state of the array
        fishes[i] += 1
    for i in range(days):
        # print(fishes)
        fishes[(i+7)%9] += fishes[i%9]
    return(sum(fishes))

print(lfish(256))