"""
Day 5 

Part 2
"""
import re

# change this var if the number of 
# crates is different for the input
NUM_CRATES = 9

LEN_CRATE = 4

NUM_LEVELS = 8

LINE_LENGTH = 35

stack_1 = []
stack_2 = []
stack_3 = []
stack_4 = []
stack_5 = []
stack_6 = []
stack_7 = []
stack_8 = []
stack_9 = []


with open("input.txt", 'r') as file:
    lines = file.readlines()
    # 9 x 4 = 36
   
    for line in lines[:NUM_LEVELS]:
        block = line[0:4].strip(' []')
        if block != "":
            stack_1.append(block)

        block = line[4:8].strip(' []')
        if block != "":
            stack_2.append(block)

        block = line[8:12].strip(' []')
        if block != "":
            stack_3.append(block)

        block = line[12:16].strip(' []')
        if block != "":
            stack_4.append(block)

        block = line[16:20].strip(' []')
        if block != "":
            stack_5.append(block)

        block = line[20:24].strip(' []')
        if block != "":
            stack_6.append(block)

        block = line[24:28].strip(' []')
        if block != "":
            stack_7.append(block)

        block = line[28:32].strip(' []')
        if block != "":
            stack_8.append(block)

        block = line[32:35].strip(' []')
        if block != "":
            stack_9.append(block)
            
    stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]
    for line in lines[10:]:
        temp = re.findall(r'\d+', line)
        res = list(map(int, temp))
        from_stack = res[1]-1
        to_stack = res[2]-1
        amount = res[0]

        # remove crates
        stacks[to_stack] = stacks[from_stack][:amount] + stacks[to_stack]
        # reset stack
        stacks[from_stack] = stacks[from_stack][amount:]

       
    for stack in stacks:
        print(stack[0])

