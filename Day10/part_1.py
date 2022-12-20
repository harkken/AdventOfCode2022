"""
Day 10

Part 1
"""

# addx = 2 cycles
# noop = 1 cycle

# 20, add 40... 60, 100, 140

# takes cycles
def noop(cycles) -> None:
    cycles += 1

def add_op(val, cycles):
    cycles += 1
    # check if cycle count has been reached
    if cycles == 20 or 60 or 100 or 140 or 180 or 220:
        print(cpu_reg  * cycles)
    cycles += 1
    if cycles == 20 or 60 or 100 or 140 or 180 or 220:
        print(cpu_reg  * cycles)
    return val

def parse_add(line) -> int:
    line = line.strip()
    if "-" in line:
        val = line.strip("-addx ")
        val = int(val) * -1
    else:
        val = line.strip("addx ")
        val = int(val)
    return val

def print_signal_strength(cycles, cpu_reg):
    print("Cycles: " + str(cycles) + " " +  str(cpu_reg * cycles))

#from ipdb import set_trace; set_trace()
count = 0
cpu_reg = 1
cycles = 0
#signal_strengh = cpu_reg * cycles
with open("input.txt", "r") as file:
    for line in file:
        if "addx" in line:
            val = parse_add(line)
            cycles += 1
            # check if cycle count has been reached
            if cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220:
                print_signal_strength(cycles, cpu_reg)
                count += cycles * cpu_reg
            cycles += 1
            if cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220:
                print_signal_strength(cycles, cpu_reg)
                count += cycles * cpu_reg
            # 2 cycles passed, update register
            cpu_reg += val

        elif "noop" in line:
            cycles += 1

print(count)

