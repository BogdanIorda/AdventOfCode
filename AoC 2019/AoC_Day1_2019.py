"""
Part 1
"""

import math

with open("C:\\Users\\40753\\Desktop\\AoC materials\\2019\\Day1\\data.txt") as file:
    file_content = file.read()
    data_list = file_content.split()
    data_list = [int(num) for num in data_list]

result = 0
for i in data_list:
    y = i / 3
    x = math.floor(y) - 2
    result += x
print(result)

"""
Part 2
"""

"""
Recursive
"""


def calculate_fuel(mass):
    fuel = max(math.floor(mass / 3) - 2, 0)
    if fuel > 0:
        fuel += calculate_fuel(fuel)
    return fuel


total_fuel = sum(calculate_fuel(mass) for mass in data_list)
print(f"Total fuel required: {total_fuel}")

"""
Iterative
"""


def fuel(mass1):
    return mass1 // 3 - 2


def total_fuel(mass):
    total_mass = 0
    while (mass := fuel(mass)) > 0:
        total_mass += mass
    return total_mass


def data_manipulation():
    with open("C:\\Users\\40753\\Desktop\\AoC materials\\2019\\Day1\\data.txt") as file:
        return sum(total_fuel(int(mass)) for mass in file)


result = data_manipulation()
print(result)
