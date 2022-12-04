import pathlib
import sys


def parse1(input_file):
    f = open(input_file)
    x = f.readlines()
    f.close()
    y = []
    for i in x:
        y.append(i.strip())
    return y


def parse2(input_file):
    f = open(input_file)
    x = f.readlines()
    f.close()
    y = []
    temp = []
    for i in x:
        temp.append(i.strip())
        if len(temp) == 3:
            y.append(temp)
            temp = []
    return y


def part1(input_arr):
    pismenka = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = 0
    for i in input_arr:
        first = i[0:len(i)//2]
        second = i[len(i)//2:]
        for p in pismenka[1:]:
            if p in first and p in second:
                out += pismenka.index(p)
    return out


def part2(input_arr):
    pismenka = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = 0
    for i in input_arr:
        for p in pismenka[1:]:
            if p in i[0] and p in i[1] and p in i[2]:
                out += pismenka.index(p)
    return out
