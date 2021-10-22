#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    preambleLength = 25
    importantNumber = 25
    print('part1:')
    for idx, line in enumerate(data[preambleLength:]):
        if findSum(data[idx: idx + importantNumber], int(line)) == False:
            print(line)
            return int(line)
            break


def findSum(arr, total):
    for num1 in arr:
        for num2 in arr:
            if num1 == num2:
                continue
            if int(num1) + int(num2) == int(total):
                return True
    return False

def part2(data, desiredTotal):
    print("part2")
    total = 0
    for idx, line in enumerate(data):
        total = int(line)
        for idx1, line1 in enumerate(data[idx+1:]):
            total += int(line1)
            if total == desiredTotal:
                sumRange = data[idx:idx+idx1]
                sumRange = [int(x) for x in sumRange]
                print(min(sumRange) + max(sumRange))
                return
            elif total > desiredTotal:
                break
            


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        part1Result = part1(data)
        part2(data, part1Result)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
