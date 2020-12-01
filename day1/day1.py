#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    found = False
    for line1 in data:
        n1 = int(line1)
        if n1 > 2020:
            continue
        for idx, line2 in enumerate(data):
            n2 = int(line2)
            if idx == 0 or n2 > 2020:
                continue
            if n1 + n2 == 2020:
                solution = n1 * n2
                print(solution)
                return solution


def part2(data):
    print('part2:')
    for line1 in data:
        n1 = int(line1)
        if n1 > 2020:
            continue
        for idx, line2 in enumerate(data):
            n2 = int(line2)
            if idx == 0 or n2 > 2020:
                continue
            for idx1, line3 in enumerate(data):
                n3 = int(line3)
                if idx == 1 or n3 > 2020:
                    continue
                currentSum = n1 + n2
                if currentSum > 2020:
                    break
                if currentSum + n3 == 2020:
                    solution = n1 * n2 * n3
                    print(solution)
                    return solution


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        start_time = time.time()
        assert part1(data) == 1020084
        assert part2(data) == 295086480
        print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
