# --*-- encoding: utf-8 --*--


from os import major


file = open("data/input.txt", "rb")
data = file.readlines()
file.close()

epsilonBit = 0
gammaBit = 0

gamma = ""
epsilon = ""


for index in range(len(data[0]) - 1):
    # print(index)
    diagnoctic = [bit[int(index)] for bit in data]
    gammaBit = int(diagnoctic.count("1") > (len(diagnoctic)/ 2))
    epsilonBit = int(not gammaBit)
    # print(diagnoctic, diagnoctic.count("1"), len(diagnoctic), gammaBit, epsilonBit)
    gamma += str(gammaBit)
    epsilon += str(epsilonBit)

print(gamma, epsilon, int(gamma, 2), int(epsilon, 2), int(gamma, 2)*int(epsilon, 2))


