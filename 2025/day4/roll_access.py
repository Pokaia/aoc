#!/usr/bin/env python3

from sys import argv

print("Day 3")

# read input file
puzzle_input = []
with open(argv[1]) as file:
    for line in file:
        row = []
        for c in line.strip():
            row.append(c)
        puzzle_input.append(row)

# print(puzzle_input)

print("Part 1")

rolls_accessible = 0

for r in range(0, len(puzzle_input)):
    for c in range(0, len(puzzle_input[r])):
        if puzzle_input[r][c] == '@': # is a roll
            # print("---------")
            # print("Current Roll: " + str(r) + ',' + str(c))
            # now check the spots around
            sum_adjacent = 0
            for y in range(c - 1, c + 2):
                for x in range(r - 1, r + 2):
                    # print("Test: " + str(x) + "," + str(y))
                    if x >= 0 and x < len(puzzle_input):
                        if y >= 0 and y < len(puzzle_input[r]):
                            if not (x == r and y == c):
                                # print("Checking: " + str(x) + "," + str(y))
                                if puzzle_input[x][y] == '@':
                                    # print("Roll Found")
                                    sum_adjacent += 1
                                # else:
                                #     print("No Roll Found")
            if sum_adjacent < 4:
                rolls_accessible += 1

print("Rolls Accessible: " + str(rolls_accessible))

print()
print("Part 2")

rolls_accessible = 0

roll_removed = True
while roll_removed:
    roll_removed = False
    for r in range(0, len(puzzle_input)):
        for c in range(0, len(puzzle_input[r])):
            if puzzle_input[r][c] == '@': # is a roll
                # print("---------")
                # print("Current Roll: " + str(r) + ',' + str(c))
                # now check the spots around
                sum_adjacent = 0
                for y in range(c - 1, c + 2):
                    for x in range(r - 1, r + 2):
                        # print("Test: " + str(x) + "," + str(y))
                        if x >= 0 and x < len(puzzle_input):
                            if y >= 0 and y < len(puzzle_input[r]):
                                if not (x == r and y == c):
                                    # print("Checking: " + str(x) + "," + str(y))
                                    if puzzle_input[x][y] == '@':
                                        # print("Roll Found")
                                        sum_adjacent += 1
                                    # else:
                                    #     print("No Roll Found")
                if sum_adjacent < 4:
                    rolls_accessible += 1
                    puzzle_input[r][c] = '.'
                    roll_removed = True

print("Rolls Removed: " + str(rolls_accessible))

