"""
Advent of Code

Day 1: Calorie Counting

Part 1
"""

with open("input.txt", "r") as file:
    """
    For each line in the file, count the lines that are grouped together
    That is, count the lines that are not new lines (\n)
    """
    total = 0
    count = 0
    for line in file:
        if line != "\n":
            count += int(line)
        if line == "\n":
            if count > total:
                total = count
            count = 0
    print(total)