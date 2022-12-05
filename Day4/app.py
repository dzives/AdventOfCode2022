def parse(input_file):
    f = open(input_file)
    x = f.readlines()
    f.close()
    y = []
    for i in x:
        temp = i.split(",")
        t = [temp[0].split('-'), temp[1].strip().split("-")]
        t[0][0], t[0][1], t[1][0], t[1][1] = int(t[0][0]), int(t[0][1]), int(t[1][0]), int(t[1][1])
        y.append(t)
    return y


def part1(input_arr):
    out = 0
    for i in input_arr:
        if i[0][0] <= i[1][0] and i[0][1] >= i[1][1]:
            out += 1
        elif i[0][0] >= i[1][0] and i[0][1] <= i[1][1]:
            out += 1
    return out


def part2(input_arr):
    out = 0
    for i in input_arr:
        for j in range(i[0][0], i[0][1]+1):
            if j in range(i[1][0], i[1][1]+1):
                out += 1
                break
    return out
