#!/usr/bin/env python3
# coding: utf-8


import os
import re
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


bagexp = re.compile("^(\d+) ([a-z ]+) bags?\.?$")


def count_bags(bag):
    count, description = bagexp.match(bag).groups()
    return (int(count), description)


def ruleparser(rule):
    main_bag, contents = rule.split(" bags contain ")
    if contents == "no other bags.":
        return main_bag, []
    return main_bag, [count_bags(bag) for bag in contents.split(', ')]


def contains_gold(bag_name, rules):
    if bag_name == "shiny gold":
        return True
    return any(contains_gold(name, rules) for _, name in rules[bag_name])


def count_containing(bag_name, rules):
    return 1 + sum(count * count_containing(name, rules) for count, name in rules[bag_name])


def part1(rules):
    print('part1:')
    print(sum((contains_gold(name, rules) and 1 or 0) for name in rules if name != "shiny gold"))


def part2(rules):
    print('part2:')
    print(count_containing("shiny gold", rules) - 1)


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        rules = dict([ruleparser(line) for line in data])
        part1(rules)
        part2(rules)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
