def number(lines):
    # a = 1
    # lines2 = []
    # for i in lines:
    #     lines2.append(f'{a}: {i}')
    #     a +=1
    # print(f'{d})
    # print(lines2)

    # def number(lines):
    #     return ['%d: %s' % v for v in enumerate(lines, 1)]

    def number(lines):
        return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

number([])
number(["a", "b", "c"])