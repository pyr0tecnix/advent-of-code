# --*-- encoding: utf-8 --*--

file = open("data/sample.txt", "r")
initial = file.readlines()
file.close()

lanternfish = []
# Utilities



days = range(1, 12)

lanternfish = initial[0]
lanternfish = list(map(int, lanternfish.split(",")))
countMultiple = map = [1 for i in range(5)]
print(countMultiple)
count = 0
buffer = 0
bufferNeeded = 0
print("Initial state: {}".format(lanternfish))
for day in days:
    babies = []
    # Lanternship
    for key, lantern in enumerate(lanternfish):
        # print(lanternfish)
        # Make a new lantern and reinit
        if bufferNeeded:
            print("Buffer {}".format(buffer))
            count += buffer
            bufferNeeded = 0
        if lantern == 0:
            
            lanternfish[key] = 6
            # babies.append(8)
            if countMultiple[key] < 2:
                print("Key : {}, {}".format(key, countMultiple))
                count += (1 * (countMultiple[key]))
            else:
                bufferNeeded = 1
                buffer = 1 * countMultiple[key] - 1

            countMultiple[key] += 1
            print("\n")
        if lantern > 0:
            lanternfish[key] -= 1

    if babies:
        # print("Babies {}".format(babies))
        lanternfish += babies

    # print("After {} day(s) :{} at total {}".format(day, lanternfish, len(lanternfish)))
    print("After {} day(s) :{} at total {}".format(day, lanternfish, (5+count)))

print("At the end : {}".format(len(lanternfish)))
print(count)