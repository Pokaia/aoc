#!/usr/bin/env python3

import sys

print("Starting Day 1")

input = []

for line in sys.stdin:
    line = line.strip()
    direction = line[0]
    number = int(line[1:])
    if direction == 'L':
        number *= -1
    input.append(number)

def part1(x):
    print("\tPart 1")

    current = 50
    numzeros = 0

    for num in x:
        current += num
        if current > 99 or current < 0:
            current %= 100
        if current == 0:
            numzeros += 1

    print("\tnum zeros: " + str(numzeros) + "\n")

def part2(x):
    print("\tPart 2")

    dial = 50
    numzeros = 0

    # brute force attack

    for num in x:
        print('-')
        print(num)
        print('-')
        operation = 1
        if num < 0:
            operation = -1

        number = abs(num)
        for i in range(0, number):
            dial += operation
            if dial > 99 or dial < 0:
                dial %= 100
            if dial == 0:
                numzeros += 1
            # print(dial)

    print("\tnum zeros: " + str(numzeros) + "\n")

part1(input)
part2(input)

