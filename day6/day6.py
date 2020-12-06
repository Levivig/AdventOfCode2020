#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    counts = []
    for idx, line in enumerate(data):
        d = {}
        letters = line.replace('\n','')

        for c in letters:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1
        counts.append(len(d))
    print(sum(counts))


def part2(data):
    print('part2:')
    counts = []
    total = 0
    for idx, line in enumerate(data):
        letters = line.replace('\n','')
        d = {}
        for c in letters:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1
    
        for char, count in d.items():
            if count == len(line.split('\n')):
                total += 1

    counts.append(total)
    print(sum(counts))


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().split('\n\n')
        part1(data)
        part2(data)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
