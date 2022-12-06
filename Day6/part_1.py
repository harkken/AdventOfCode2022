"""
Day 6 

Part 1
"""

with open("input.txt", 'r') as file:
    data = file.read()
    leng = len(data)-4
    start = 0
    end = 14
    for letter in data[:leng]:
        block = data[start:end]
        if len(set(block)) == 4:
            print(end)
            break
        start += 1
        end += 1