#!/usr/bin/env python3

import sys

input_file = sys.argv[1]

puzzle_input = []
with open(input_file, 'r') as file:
    for line in file:
        puzzle_input.append(line.strip())

print('-----------')
print('Part 1')

total_output_voltage = 0
for bank in puzzle_input:
    # print(bank)
    bank_voltage = 0
    for i in range(0, len(bank) - 1):
        for j in range(i + 1, len(bank)):
            possible_bank_joltage = int(bank[i] + bank[j])
            if possible_bank_joltage > bank_voltage:
                bank_voltage = possible_bank_joltage
    # print("Bank Voltage: " + str(bank_voltage))
    total_output_voltage += bank_voltage
    # print("Total Voltage: " + str(total_output_voltage))

print("Total Output Joltage: " + str(total_output_voltage))

print('-----------')
print('Part 2')

total_output_joltage = 0
for bank in puzzle_input:
    current_batteries = bank[:12] 
    current_max_joltage = int(current_batteries)
    for i in range(12, len(bank)):
        # print("cur: " + current_batteries)
        # print("add: " + bank[i])
        test_batteries = current_batteries + bank[i]
        # print("new: " + test_batteries)
        current_max_joltage = 0
        for j in range(0, len(test_batteries)):
            test = test_batteries[:j] + test_batteries[j+1:]
            test_joltage = int(test)
            # print("tst: " + test)
            if test_joltage > current_max_joltage:
                current_batteries = test
                current_max_joltage = test_joltage

    total_output_joltage += current_max_joltage


print("Total Output Joltage: " + str(total_output_joltage))

