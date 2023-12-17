"""
Part 1
"""

with open("C:\\Users\\40753\\Desktop\\AoC materials\\2017\Day1\\input.txt") as file:
    data = file.read().split()
    data = [int(num) for num in data]

digits = [int(digit) for digit in str(data[0])]

sum_of_data = 0

for i in range(len(digits)):
    if digits[i] == digits[(i + 1) % len(digits)]:
        sum_of_data += digits[i]
print(sum_of_data)

"""
Part 2
"""

sum_of_data2 = 0
digits_length = len(digits)
for n in range(digits_length):
    half_way = (n + digits_length // 2) % digits_length
    if digits[n] == digits[half_way]:
        sum_of_data2 += digits[n]
print(sum_of_data2)

print(digits[1000])
print(digits[1])
