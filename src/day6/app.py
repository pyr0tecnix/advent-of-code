# --*-- encoding: utf-8 --*--

file = open("data/input.txt", "r")
initial = file.readlines()
file.close()

lanternfish = []
# Utilities



days = range(1, 81)

lanternfish = initial[0]
lanternfish = list(map(int, lanternfish.split(",")))

print("Initial state: {}".format(lanternfish))
for day in days:
    babies = []
    # Lanternship
    for key, lantern in enumerate(lanternfish):
        # print(lanternfish)
        # Make a new lantern and reinit
        if lantern == 0:
            lanternfish[key] = 6
            babies.append(8)
        
        if lantern > 0:
            lanternfish[key] -= 1

    if babies:
        # print("Babies {}".format(babies))
        lanternfish += babies

    # print("After {} day(s) :{}".format(day, lanternfish))

print("At the end : {}".format(len(lanternfish)))