"""
Day 10

Part 2
"""

# addx = 2 cycles
# noop = 1 cycle



def parse_add(line) -> int:
    line = line.strip()
    if "-" in line:
        val = line.strip("-addx ")
        val = int(val) * -1
    else:
        val = line.strip("addx ")
        val = int(val)
    return val



def draw_pixel(cur_row: int, crt: list, cycle: int, sprite_row: list) -> None:
    """
    Draw pixel (lit or unlit on row)
    
    If row is 1, draw '#' else draw '.'
    """

    pos = (cycle % 40) - 1
    crt[cur_row][pos] = '#' if sprite_row[pos] else '.'



sprite_row = [0] * 40
sprite_row[:3] = [1,1,1]

count = 0
cpu_reg = 1
cycles = 0 # cur_pos
cur_row = 0

# set up CRT monitor
# 40 x 6
crt = []
for row in range(6):
    crt_row = [0] * 40
    crt.append(crt_row)

# Order of operations
'''
- caclulate current sprite position on the row
- check if it matches with the current sprite row
    - probably easiest to create an OR function
    - nvm, easiest to have 1's and 0's for everything
'''


with open("input.txt", "r") as file:
    for line in file:
        if "addx" in line:
            val = parse_add(line)
            cycles += 1
            draw_pixel(cur_row, crt, cycles, sprite_row)
            if cycles % 40 == 0:
                cur_row +=1 
            cycles += 1
            draw_pixel(cur_row, crt, cycles, sprite_row)
            if cycles % 40 == 0:
                cur_row +=1 
            # 2 cycles passed, update register
            cpu_reg += val
            # update_sprite_row
            pos = cpu_reg
            sprite_row = [0] * 40
            sprite_row[pos-1:pos+1] = [1,1,1]

        elif "noop" in line:
            cycles += 1
            draw_pixel(cur_row, crt, cycles, sprite_row)
            if cycles % 40 == 0:
                cur_row +=1 


for line in crt:
    print(line)

