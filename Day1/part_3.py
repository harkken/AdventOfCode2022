"""
Advent of Code

Day 1: Calorie Counting

Part 2 - but worse
"""

with open("input.txt", "r") as file:
    """
    For each line in the file, count the lines that are grouped together
    That is, count the lines that are not new lines (\n)
    
    """
    li = []
    count = 0
    for line in file:
        if line != "\n":
            count += int(line)
        if line == "\n":
            li.append(count)
            count = 0

    li = sorted(li)
    leng = len(li)
    print( li[leng-1])
    print( li[leng-2])
    print( li[leng-3])

