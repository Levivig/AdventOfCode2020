#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    intData = [int(x) for x in data]
    intData = sorted(intData)
    intData.insert(0,0)
    lastIndex = len(intData) - 1
    intData.append(intData[lastIndex] + 3)
    print(intData)
    res = {"1": 0,"2": 0,"3": 0}
    for idx,line in enumerate(intData):
        if idx == len(intData) - 1:
            break
        line1 = intData[idx+1]
        if line1 - line == 1:
            res["1"] += 1
        elif line1 - line == 2:
            res["2"] += 1
        elif line1 - line == 3:
            res["3"] += 1
    print(res["1"] * res["3"])


def part2(data):
    print('part2:')
    for line in data:
        pass
        # print(line)


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        part1(data)
        part2(data)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
