#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    x = 0
    y = 0

    trees = 0
    for line in data:
        lineLenght = len(line)
        currentItem = line[x%lineLenght]
        if currentItem == "#":
            trees += 1
        x += 3
        y += 1
    print(trees)
    return trees


def part2(data):
    print('part2:')
    x = [0,0,0,0,0]
    y = [0,0,0,0,0]

    moves = [(1,1), (3,1), (5,1), (7,1),(1,2)] 

    trees = [0,0,0,0,0]
    for n, line in enumerate(data):
        lineLenght = len(line)

        for idx, move in enumerate(moves):
            if idx == 4 and n % 2 != 0:
                continue
            currentX = x[idx]
            currentY = y[idx]

            currentItem = line[currentX%lineLenght]
            if currentItem == "#":
                trees[idx] += 1
            x[idx] += int(move[0])
            y[idx] += int(move[1])

    print(trees)

    mult = 1
    for tree in trees:
        mult *= tree
    print(mult)

    return mult


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        start_time = time.time()
        assert part1(data) == 209
        assert part2(data) == 1574890240
        print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
