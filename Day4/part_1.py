"""
Day 4

Part 1 - Corrrect Version
"""
count = 0

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        chunk_1, chunk_2 = line.split(',')
        one = chunk_1.split('-')
        two = chunk_2.split('-')
        li1 = [*range(int(one[0]), int(one[1])+1)]
        li2 = [*range(int(two[0]), int(two[1])+1)]
        if set(li1).issubset(set(li2)) or set(li2).issubset(set(li1)):
            count += 1
    print(count)

