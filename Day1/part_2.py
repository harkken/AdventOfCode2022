"""
Advent of Code

Day 1: Calorie Counting

Part 2
"""

with open("input.txt", "r") as file:
    li = [0,0,0]
    count = 0
    for line in file:
        if line != "\n":
            count += int(line)
        if line == "\n":
            for item in li:
                if count > item:
                    li.append(count)
                    li = sorted(li)
                    li = li[1:]
                    count = 0
                    break
            count = 0    
    print(li)
    print(li[0] + li[1] + li[2])            
