#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def toBinaryString(text):
    ret = []
    for c in text:
        if c == 'F' or c == 'L':
            ret.append('0')
        elif c == 'B' or c == 'R':
            ret.append('1')
    return ''.join(ret)


def part1(data):
    print('part1:')
    answer = max(data)
    
    print(answer)
    return answer



def part2(data):
    print('part2:')
    missing = [x for x in range(data[0], data[-1]+1) if x not in data] 
    answer = missing[0]

    print(answer)
    return answer


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        idList = []
        for line in data:
            row = int(toBinaryString(line[:7]), 2)
            column = int(toBinaryString(line[-3:]), 2)

            idx = row * 8 + column
            idList.append(idx)

        idList.sort()

        assert part1(idList) == 933
        assert part2(idList) == 711


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
