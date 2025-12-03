#!/usr/bin/env python3

import sys

input_file = sys.argv[1]

puzzle_input = ''
with open(input_file, 'r') as file:
    line = file.readline()
    puzzle_input = line.strip()

# print('Puzzle input:')
# print(puzzle_input)

def detect_pattern_part1(test):
    if test[0] == '0':
        return False
    if len(test) % 2 > 0: # odd
        return False
    # check first half with second
    middle = len(test) // 2
    first_half = test[:middle]
    second_half = test[middle:]
    # print("First: " + first_half)
    # print("Second: " + second_half)
    if first_half == second_half:
        return True
    return False

def detect_pattern(test):
    if test[0] == '0':
        return False
    if len(test) % 2 > 0: # odd
        return False
    # check first half with second
    middle = len(test) // 2
    first_half = test[:middle]
    second_half = test[middle:]
    # print("First: " + first_half)
    # print("Second: " + second_half)
    if first_half == second_half:
        return True
    return False

# print(detect_pattern('11'))
# print(detect_pattern('1010'))
# print(detect_pattern('101'))
# print(detect_pattern('0101'))
# print(detect_pattern('1188511885'))
# print(detect_pattern('222222'))
# print(detect_pattern('446446'))
# print(detect_pattern('38593859'))

id_ranges = []
ranges = puzzle_input.split(',')
for r in ranges:
    limits = []
    for part in r.split('-'):
        limits.append(part)
    id_ranges.append(limits)

# print(id_ranges)
        
print("Part 1")

sum_of_invalid = 0
for id_range in id_ranges:
    for i in range(int(id_range[0]), int(id_range[1]) + 1):
        if detect_pattern_part1(str(i)):
            # print('found: ' + str(i))
            sum_of_invalid += i

print('Sum of invalid: ' + str(sum_of_invalid))

def detect_pattern(test):
    # print("-\nTesting: " + test)
    if test[0] == '0':
        return False
    for i in range(1, len(test) // 2 + 1):
        substring = test[:i]
        # print("substring: " + substring)
        splits = test.split(substring)
        # print(splits)
        matched = True
        for s in splits:
            if len(s) > 0:
                matched = False
        if matched:
            # print(test)
            return True
    return False

print("\nPart2")
sum_of_invalid = 0
for id_range in id_ranges:
    for i in range(int(id_range[0]), int(id_range[1]) + 1):
        if detect_pattern(str(i)):
            # print('found: ' + str(i))
            sum_of_invalid += i

print('Sum of invalid: ' + str(sum_of_invalid))
