from app import *
from time import time
from termcolor import colored
import os

if __name__ == '__main__':
    os.system('color')
    p1c = 95437
    p2c = 24933642
    path = 'sample.txt'
    print(f'{path}: ', end='\n')
    parsed = parse(path)
    start = time()
    p1r = part1(parsed)
    end = time()
    p1t = end-start
    if p2c:
        start = time()
        p2r = part2(parsed)
        end = time()
        p2t = end-start
    if p1c == p1r:
        print(colored('Part 1 sample is correct.', 'green'))
    else:
        print(colored('Part 1 sample is incorrect.', 'red'))
    if p2c is None:
        print(colored('Part 2 sample is not defined.', 'yellow'))
    elif p2c == p2r:
        print(colored('Part 2 sample is correct.', 'green'))
    else:
        print(colored('Part 2 sample is incorrect.', 'red'))
    print(f'Part 1: {p1r}|Time: {p1t:.3f}s')
    if p2c:
        print(f'Part 2: {p2r}|Time: {p2t:.3f}s')
    path = 'input.txt'
    print(f'{path}: ', end='\n')
    parsed = parse(path)
    start = time()
    p1r = part1(parsed)
    end = time()
    p1t = end-start
    if p2c:
        start = time()
        p2r = part2(parsed)
        end = time()
        p2t = end-start
    print(f'Part 1: {p1r}|Time: {p1t:.3f}s')
    if p2c:
        print(f'Part 2: {p2r}|Time: {p2t:.3f}s')
