"""
Day 4

Part 1

Now I know how to compare sets
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
        set_1 = set(li1)
        set_2 = set(li2)
        intersect = set_1.intersection(set_2)
        if set_1 == intersect or set_2 == intersect:
            count += 1
    print(count)
