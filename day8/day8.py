#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


# def part1(data):
#     print('part1:')
#     print(runMachine(data))


# def runMachine(data):
#     accumulator = 0
#     currentLine = 0
#     history = [0 for x in range(0,len(data))]
#     finished = False
#     while True:
#         line = data[currentLine]
#         operation, value = tuple(line.split(" "))
#         if operation == "acc":
#             accumulator += int(value)
#             history[currentLine] += 1
#             currentLine += 1
#         elif operation == "nop":
#             history[currentLine] += 1
#             currentLine += 1
#         elif operation == "jmp":
#             jumpVal = int(value)
#             history[currentLine] += 1
#             if jumpVal < 0:
#                 jumpVal -= 1
#             currentLine += jumpVal
#         if currentLine >= len(data):
#             finished = True
#             break
#         if history[currentLine] >= 1:
#             finished = False
#             break

#     return accumulator, finished


# def flip(idx, data):
#     if data[idx][:3] == 'jmp':
#         currentData = data[idx]
#         currentData = currentData.replace('jmp','nop')
#         data[idx] = currentData
#     elif data[idx][:3] == 'nop':
#         currentData = data[idx]
#         currentData = currentData.replace('nop','jmp')
#         data[idx] = currentData
#     return data


# def part2(data):
#     print('part2:')
#     changePos = 0
#     operations = data
#     while True:
#         operations = flip(changePos, operations)

#         score, finished = runMachine(operations)
#         if finished == False:
#             data = flip(changePos, operations)
#             changePos += 1
#         else:
#             break
#         if changePos >= len(operations):
#             break
#     print(score)


# def main():
#     currentDay = os.path.basename(__file__).split('.')[0]
#     print(currentDay)
#     with open(inputfile) as f:
#         data = f.read().splitlines()
#         # part1(data)
#         part2(data)


# if __name__ == "__main__":
#     start_time = time.time()
#     main()
#     print("--- %s seconds ---" % (time.time() - start_time))

lines = open(inputfile).read().splitlines()
ops=[]
for line in lines:
    op, val = line.split()
    val=int(val)
    ops.append((op,val))

def accumulator(ops):
    repeat=False
    accumulator=i=0
    ran=set()
    while i<len(ops):
        if i in ran:
            repeat=True
            break
        ran.add(i)
        op,val=ops[i]
        if op=='acc':accumulator+=val
        elif op=='jmp':i+=val-1
        i+=1
    return accumulator, repeat
print("Part 1:",accumulator(ops)[0])

swap={'nop':'jmp','jmp':'nop'}
for i,(op,val) in enumerate(ops):
    if op in ['nop','jmp']:
        acc,rep = accumulator(ops[:i]+[(swap[op],val)]+ops[i+1:])
        if not rep: print("Part 2:",acc)