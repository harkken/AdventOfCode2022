"""
Day 3

Advent of Code

"""

'''
Each rucksack has two large compartments

All items of one type go into a compartment

One type per rucksack is in the wrong compartment

lowercase and uppercase items are different

first half is first compartment, second half is the second compartment

The rucksacks will both half 1 item each that has been put in both compartments

a -> z = 1 -> 26

A -> Z 27 -> 52

'''

"""
notes: 
- We can assume that each line is an even length
"""

sum = 0

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


with open("input.txt", "r") as f:

    for line in f:
        line = line.strip()
        total_length = len(line)
        first_half = line[:int(total_length/2)]
        second_half = line[int(total_length/2):]
        items_first = set(first_half)
        items_second = set(second_half)
        item = list(items_first.intersection(items_second))
        if alphabet.find(item[0]) == -1:
            sum+= (alphabet_caps.find(item[0]) +1) +26
        sum+= (alphabet.find(item[0]) + 1)  
    
    print(sum)
