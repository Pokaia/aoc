#!/usr/bin/env python3

from sys import argv

print("Day 5")

# read puzzle input

fresh_ranges = []
ingredients = []

with open(argv[1]) as file:
    ranges_complete = False
    for line in file:
        line = line.strip()
        if len(line) == 0:
            ranges_complete = True
        elif not ranges_complete:
            # read range
            range_str = line.split('-')
            fresh_ranges.append([int(range_str[0]), int(range_str[1])])
        else:
            # read ingredient
            ingredients.append(int(line))

# print("Fresh Ranges:")
# print(fresh_ranges)
# print("Ingredients:")
# print(ingredients)

print("Part 1")

fresh_ingredients = 0
for i in ingredients:
    for r in fresh_ranges:
        if i >= r[0] and i <= r[1]:
            fresh_ingredients += 1
            break;
            # don't need to keep going
            # in fact, only want to increment once per ingredient so better break

print("Fresh ingredients: " + str(fresh_ingredients))

print()
print("Part 2")

range_limits = []
for r in fresh_ranges:
    range_limits.append((r[0], 0, 1))
    range_limits.append((r[1], 1, -1))

range_limits.sort()
# print(range_limits)

sum_fresh_ingredient_ids = 0
depth = 0
start = 0
for value, _, depth_change in range_limits:
    if depth == 0 and depth_change == 1:
        start = value
    depth += depth_change
    if depth == 0:
        sum_fresh_ingredient_ids += value - start + 1

print("Number of fresh ingredient IDs: " + str(sum_fresh_ingredient_ids))
