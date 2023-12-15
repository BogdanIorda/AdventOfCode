"""
Part 1
"""

with open("C:\\Users\\40753\\Desktop\\AoC materials\\2018\Day1\\input.txt") as file:
    data = file.read().split()
    data = [int(num) for num in data]

result = 0
for num in data:
    result += num

print(result)

"""
Part 2
"""

with open("C:\\Users\\40753\\Desktop\\AoC materials\\2018\Day1\\input.txt") as file:
    data = [int(line.strip()) for line in file]

freq_found = set()

freq = 0
index = 0
freq_duplicate = False

while not freq_duplicate:
    freq += data[index]
    if freq in freq_found:
        freq_duplicate = True
    else:
        freq_found.add(freq)
        index = (index + 1) % len(data)

print(f"First Frequency is: {freq}")
