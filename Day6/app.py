import pathlib
import sys


def parse(input_file):
    f = open(input_file)
    x = f.readlines()
    f.close()
    return x[0]


def part1(input):
    for i in range(len(input)):
        if i < 3:
            continue
        if len(set(list(input[i-4:i]))) == 4:
            return i
    raise RuntimeError


def part2(input):
    for i in range(len(input)):
        if i < 13:
            continue

        if len(set(list(input[i-14:i]))) == 14:
            return i

    raise RuntimeError
