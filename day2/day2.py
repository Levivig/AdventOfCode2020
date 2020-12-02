#!/usr/bin/env python3
# coding: utf-8


import os
from operator import xor
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    correct_count = 0
    for line in data:
        splitted = line.split(" ")
        rule = splitted[0].split('-')
        letter = splitted[1][0]
        password = splitted[2]

        occurance = password.count(letter)
        min_rule = int(rule[0])
        max_rule = int(rule[1])

        if occurance in range(min_rule, max_rule + 1):
            correct_count += 1

    print(correct_count)
    return correct_count


def part2(data):
    print('part2:')
    correct_count = 0
    for line in data:
        splitted = line.split(" ")
        rule = splitted[0].split('-')
        letter = splitted[1][0]
        password = splitted[2]

        first_rule = int(rule[0]) - 1
        second_rule = int(rule[1]) - 1

        if xor(password[first_rule] == letter, password[second_rule] == letter):
            correct_count += 1
    
    print(correct_count)
    return correct_count


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        start_time = time.time()
        assert part1(data) == 469
        assert part2(data) == 267
        print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
