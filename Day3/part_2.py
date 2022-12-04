"""
Day 3 

Part 2
"""
count = 0

sum = 0

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open("input.txt", "r") as file:
    # split into lines
    first = 0
    second = 3
    lines = file.readlines()
    while count < 100:
        block = lines[first:second]
        set_1 = set(block[0].strip())
        set_2 = set(block[1].strip())
        set_3 = set(block[2].strip())

        inter_1 = set_1.intersection(set_2)
        item = list(inter_1.intersection(set_3))
        first += 3
        second += 3
        count += 1
        if alphabet.find(item[0]) == -1:
            sum+= (alphabet_caps.find(item[0]) +1) +26
        sum+= (alphabet.find(item[0]) + 1)  

    print(sum)