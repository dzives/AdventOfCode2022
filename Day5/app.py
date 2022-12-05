import pathlib
import sys
from re import findall


def parse(input_file):
    f = open(input_file)
    x = f.readlines()
    f.close()
    stacks = []
    y = []
    for i in x:
        y.append(i.replace("\n", "").replace("[", " ").replace("]", " "))
    y, ins = y[:y.index("")-1], y[y.index("")+1:]
    for j in range(len(y[0])):
        temp = []
        for i in range(len(y)):
            if y[i][j] != " ":
                temp.append(y[i][j])
        if temp:
            stacks.append(temp)
    temp = []
    for i in ins:
        temp.append(list(map(int, findall(r'\d+', i))))
    ins = temp.copy()
    return stacks, ins


def part1(stacks, ins):
    out = []
    for i in range(len(ins)):
        for j in range(ins[i][0]):
            t = stacks[ins[i][1]-1].pop(0)
            stacks[ins[i][2]-1].insert(0, t)
    for i in stacks:
        out.append(i[0])
    return "".join(out)


def pop_range(arr: list, e):
    temp = []
    print(arr, e)
    for i in range(e):
        temp.append(arr.pop())
    return temp


def part2(stacks, ins):
    out = []
    t = []
    for i in range(len(ins)):
        for j in range(ins[i][0]):
            t.append(stacks[ins[i][1]-1].pop(0))
        for x in t[::-1]:
            stacks[ins[i][2]-1].insert(0, x)
        t = []
    for i in stacks:
        out.append(i[0])
    return "".join(out)


print(part2(*parse("input.txt")))
