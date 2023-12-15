"""
Part 1
"""

with open("C:\\Users\\40753\\Desktop\\AoC materials\\2021\\Day1\\data.txt", ) as file:
    data = file.read().split()
    data = [int(n) for n in data]

comparing = data[0]
increased = 0
for num in data:
    if num > comparing:
        increased += 1
        comparing = num
    elif num < comparing:
        comparing = num

print(increased)


"""
Part 2
"""

with open("C:\\Users\\40753\\Desktop\\AoC materials\\2021\\Day1\\data.txt") as file:
    data = file.read().split()
    data = [int(n) for n in data]


def create_pairs(data):
    return [sum(data[i:i + 3]) for i in range(len(data) - 2)]


pairs_sum = create_pairs(data)
print(pairs_sum)
increased = sum(1 for i in range(len(pairs_sum) - 1) if pairs_sum[i + 1] > pairs_sum[i])

print(increased)
