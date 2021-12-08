

from os import remove


def decode7segment():
    with open('data/sample.txt') as file:
        data = file.readlines()
        signals = [line.split("|")[0].strip() for line in data]
        outputs = [line.split("|")[1].strip() for line in data][0]
        outputs = outputs.split(" ")

    total = 0
    for signal in signals:
        s = signal.split(" ")
        digit = dict()
        # print(s)
        # Identify obvious
        digit[1] = list(filter(lambda x: len(x) == 2, s))[0]
        digit[4] = list(filter(lambda x: len(x) == 4, s))[0]
        digit[7] = list(filter(lambda x: len(x) == 3, s))[0]
        digit[8] = list(filter(lambda x: len(x) == 7, s))[0]

        # 2, 3, 5
        fivePattern = list(filter(lambda x: len(x) == 5, s))
        # 0, 6, 9
        sixPattern = list(filter(lambda x: len(x) == 6, s))
        print("What we know : {}".format(digit))
        print("Five pattern : {}".format(fivePattern))
        print("Six pattern : {}".format(sixPattern))

        # 3 is to only to contain 1
        # print(digit[1][0])
        digit[3] = list(filter(lambda x: all(item in x for item in digit[1]), fivePattern))[0]
        print("3 : {}".format(digit[3]))
        fivePattern.remove(digit[3])

        # 6 does not contain 1
        digit[6] = list(filter(lambda x: not all(item in x for item in digit[1]), sixPattern))[0]
        print("6 : {}".format(digit[6]))
        sixPattern.remove(digit[6])

        # 5 contain 6 3 firsts elements
        digit[5] = list(filter(lambda x: x.startswith(digit[6][:3]), fivePattern))[0]
        print("5 : {}".format(digit[5]))
        fivePattern.remove(digit[5])

        # 2 is the last element of five pattern
        digit[2] = fivePattern.pop()
        print("2 : {}".format(digit[2]))

        # 9 contain 8 4 first elements
        digit[9] = list(filter(lambda x: all(item in x for item in digit[8][:4]), sixPattern))[0]
        print("9 : {}".format(digit[9]))

        # 0 is the last element of six pattern
        digit[0] = sixPattern.pop()
        print("0 : {}".format(digit[0]))

        keys = list(digit.keys())
        vals = list(digit.values())

        # Interpret output
        result = []
        for output in outputs:
            # print(sorted(output), sorted(digit[3]))
            # print(digit[1])
            if sorted(output) == sorted(digit[0]):
                result.append("0")

            if sorted(output) == sorted(digit[1]):
                result.append("1")

            if sorted(output) == sorted(digit[2]):
                result.append("2")

            if sorted(output) == sorted(digit[3]):
                result.append("3")

            if sorted(output) == sorted(digit[4]):
                result.append("4")

            if sorted(output) == sorted(digit[5]):
                result.append("5")

            if sorted(output) == sorted(digit[6]):
                result.append("6")

            if sorted(output) == sorted(digit[7]):
                result.append("7")

            if sorted(output) == sorted(digit[8]):
                result.append("8")

            if sorted(output) == sorted(digit[9]):
                result.append("9")

        total += int("".join([item[0] for item in result]))
        print(outputs, result, int("".join([item[0] for item in result])) )
        print("-----------")
    print(total)
decode7segment()
