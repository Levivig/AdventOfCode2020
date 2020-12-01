#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    for line in data:
        print(line)


def part2(data):
    print('part2:')
    for line in data:
        print(line)


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        start_time = time.time()
        part1(data)
        part2(data)
        print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
