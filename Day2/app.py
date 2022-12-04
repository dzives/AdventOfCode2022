import pathlib
import sys


def parse(input_file):
    f = open(input_file)
    x = f.readlines()
    f.close()
    return x


def part1(input_arr):
    out = 0
    for i in input_arr:
        if i[0] == "A":
            if i[2] == "Y":
                out += 8
            elif i[2] == "X":
                out += 4
            elif i[2] == "Z":
                out += 3
        elif i[0] == "B":
            if i[2] == "Y":
                out += 5
            elif i[2] == "X":
                out += 1
            elif i[2] == "Z":
                out += 9
        elif i[0] == "C":
            if i[2] == "Y":
                out += 2
            elif i[2] == "X":
                out += 7
            elif i[2] == "Z":
                out += 6
    return out


def part2(input_arr):
    out = 0
    for i in input_arr:
        if i[0] == "A":
            if i[2] == "Y":
                out += 4
            elif i[2] == "X":
                out += 3
            elif i[2] == "Z":
                out += 8
        elif i[0] == "B":
            if i[2] == "Y":
                out += 5
            elif i[2] == "X":
                out += 1
            elif i[2] == "Z":
                out += 9
        elif i[0] == "C":
            if i[2] == "Y":
                out += 6
            elif i[2] == "X":
                out += 2
            elif i[2] == "Z":
                out += 7
    return out
