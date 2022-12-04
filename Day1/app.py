import pathlib
import sys


def parse(input_file):
    f = open(input_file)
    x = f.readlines()
    f.close()
    y = []
    elves = []
    t = []
    for i in x:
        if i == "\n":
            elves.append(t)
            t = []
        else:
            t.append(int(i))
    if t is not []:
        elves.append(t)
    return elves


def part1(input_arr):
    sums = []
    for i in input_arr:
        sums.append(sum(i))
    return max(sums)


def part2(input_arr):
    sums = []
    for i in input_arr:
        sums.append(sum(i))
    sums.sort(reverse=True)
    return sums[0]+sums[1]+sums[2]
