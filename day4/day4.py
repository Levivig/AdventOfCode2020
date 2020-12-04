#!/usr/bin/env python3
# coding: utf-8


import os
import re
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    valid = 0
    for dict in data:
        if containsAllFields(dict):
            valid += 1
    print(valid)
    return valid


def part2(data):
    print('part2:')
    valid = 0
    for dict in data:
        if containsAllFields(dict) and validate(dict):
            valid += 1
    print(valid)
    return valid


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    start_time = time.time()
    with open(inputfile) as f:
        data = f.read().split("\n\n")
        cleanData = []

        for line in data:
            passport = line.replace("\n", " ")
            passport = passport.split(" ")
            dict = {}
            for field in passport:
                pairs = field.split(':')
                dict[pairs[0]] = pairs[1]
            cleanData.append(dict)

        assert part1(cleanData) == 190
        assert part2(cleanData) == 121
        print("--- %s seconds ---" % (time.time() - start_time))


def containsAllFields(dict):

    if 'byr' not in dict.keys():
        return False
    elif dict['byr'] == None or dict['byr'] == "":
        return False

    if 'iyr' not in dict.keys():
        return False
    elif dict['iyr'] == None or dict['iyr'] == "":
        return False

    if 'eyr' not in dict.keys():
        return False
    elif dict['eyr'] == None or dict['eyr'] == "":
        return False
    
    if 'hgt' not in dict.keys():
        return False
    elif dict['hgt'] == None or dict['hgt'] == "":
        return False

    if 'ecl' not in dict.keys():
        return False
    elif dict['ecl'] == None or dict['ecl'] == "":
        return False
    
    if 'hcl' not in dict.keys():
        return False
    elif dict['hcl'] == None or dict['hcl'] == "":
        return False
    
    if 'pid' not in dict.keys():
        return False
    elif dict['pid'] == None or dict['pid'] == "":
        return False

    return True


def validate(dict):
    isValid = True

    if 'byr' in dict.keys():
        year = int(dict['byr'])
        isValid = year >= 1920 and year <= 2002

    if isValid == False:
        return False

    if 'iyr' in dict.keys():
        year = int(dict['iyr'])
        isValid = year >= 2010 and year <= 2020
    
    if isValid == False:
        return False

    if 'eyr' in dict.keys():
        year = int(dict['eyr'])
        isValid = year >= 2020 and year <= 2030
    
    if isValid == False:
        return False
        
    if 'hgt'in dict.keys():
        value = dict['hgt']
        if value[-2:] == 'cm':
            number = int(value[:-2])
            isValid = number >= 150 and number <= 193
        elif value[-2:] == 'in':
            number = int(value[:-2])
            isValid = number >= 59 and number <= 76
        else:
            isValid = False

    if isValid == False:
        return False

    if 'hcl' in dict.keys():
        value = dict['hcl']

        regex = "^#(?:[0-9a-fA-F]{3}){1,2}$"
        p = re.compile(regex)
        match = re.search(p, value)
        if match:
            isValid = True
        else:
            isValid = False

    if isValid == False:
        return False

    if 'ecl' in dict.keys():
        value = dict['ecl']
        isValid = value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth'

    if isValid == False:
        return False

    if 'pid' in dict.keys():
        value = dict['pid']
        isValid = len(value) == 9 and value.isnumeric()

    return isValid


if __name__ == "__main__":
    main()
