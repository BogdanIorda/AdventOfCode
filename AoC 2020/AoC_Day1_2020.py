"""
PART 1 : My first Solution(not optimized)
"""
with open("C:\\Users\\40753\\Desktop\\AoC materials\\2020\\Day1\\input.txt") as file:
    numbers = []
    for line in file:
        numbers.append(int(line.strip()))
    first_num = 0
    for n in numbers:
        if n != first_num:
            first_num = n
            for num in numbers:
                if first_num + num == 2020:
                    result = num * n
    print(result)

"""
PART 1 : My second Solution(Optimized)
"""
with open("C:\\Users\\40753\\Desktop\\AoC materials\\2020\\Day1\\input.txt") as file:
    numbers = []
    for line in file:
        numbers.append(int(line.strip()))
    for x in numbers:
        for y in numbers:
            if x + y == 2020:
                result = x * y
    print(result)


"""
PART 2 
"""

with open("C:\\Users\\40753\\Desktop\\AoC materials\\2020\\Day1\\input.txt") as file:
    numbers = []
    for line in file:
        numbers.append(int(line.strip()))
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if x + y + z == 2020:
                    result = x * y * z
    print(result)
