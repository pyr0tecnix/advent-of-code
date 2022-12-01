# --*-- encoding: utf-8 --*--


from os import major


file = open("data/input.txt", "rb")
data = file.readlines()
file.close()

epsilonBit = 0
gammaBit = 0

gamma = ""
epsilon = ""


def findOxgen(index, samples):
    diagnostic = [bit[int(index)] for bit in data]
    print(samples)
    needle = int(diagnostic.count("1") > (len(diagnostic)/ 2))
    if int(diagnostic.count("0")) == int(diagnostic.count("1")):
        needle = 1
    print(diagnostic, str(needle), len(samples))
    filteredSamples = []
    for key, sample in enumerate(samples):
        # print(key, sample, len(samples), sample[0], str(needle),sample.startswith(str(needle)))
        if str(sample)[index] == str(needle):
            filteredSamples.append(sample)


    return filteredSamples
        
def findCO2(index, samples):
    diagnostic = [bit[int(index)] for bit in data]
    print(samples)
    needle = int(diagnostic.count("0") > (len(diagnostic)/ 2))
    if int(diagnostic.count("0")) == int(diagnostic.count("1")):
        needle = 0
    print(diagnostic, str(needle), len(samples))
    filteredSamples = []
    for key, sample in enumerate(samples):
        # print(key, sample, len(samples), sample[0], str(needle),sample.startswith(str(needle)))
        if str(sample)[index] == str(needle):
            filteredSamples.append(sample)


    return filteredSamples
        

for index in range(len(data[0]) - 1):
    print(index)
    # print(data)
    data = findCO2(index, data)
    if len(data) == 1:
        break

print(data, int(data[0], 2))

# Oxygen 2031 - CO2 2104

# for index in range(len(data[0]) - 1):
#     # print(index)
#     diagnostic = [bit[int(index)] for bit in data]
#     gammaBit = int(diagnostic.count("1") > (len(diagnostic)/ 2))
#     epsilonBit = int(not gammaBit)
#     print(diagnostic, diagnostic.count("1"), len(diagnostic), gammaBit, epsilonBit)
#     # gamma += str(gammaBit)
#     # epsilon += str(epsilonBit)

# print(gamma, epsilon, int(gamma, 2), int(epsilon, 2), int(gamma, 2)*int(epsilon, 2))

