"""
Advent of Code
2022 - Day 9 - Rope Bridge

"""
X = 0
Y = 1
DOWN = -1   # 0, -1 - down (neg)
UP = 1      # 0, 1  - up (pos)
LEFT = -1   # -1, 0 - left  (neg)
RIGHT = 1   # 1, 0  - right (pos)


# init variables
start_position, head, tail, prev_head_pos = [0,0], [0,0], [0,0], [0,0]

# holds the positions visited by the tail
grid = [start_position]

def move_head(num_steps, axis, direction):
    global head, prev_head_pos   
    for _ in range(num_steps):
        prev_head_pos = list(head) # copy value not reference!
        head[axis] += direction
        check_tail_pos()    

def move(direction, num_steps): 
    if direction == "up":
        move_head(num_steps, Y, UP)
    elif direction == "down":
        move_head(num_steps, Y, DOWN)
    elif direction == "left":
        move_head(num_steps, X, LEFT) 
    elif direction == "right":
        move_head(num_steps, X, RIGHT)


def check_if_visited(spot):
    if spot not in grid:
        grid.append(spot)


def check_tail_pos():    
    # only need to move tail if it is two squares away
    global head, tail, prev_head_pos
    conditions_x = (head[0] + 1 == tail[0]) or (head[0] - 1 == tail[0]) or (head[0] == tail[0])
    conditions_y =  (head[1] - 1 == tail[1]) or (head[1] == tail[1]) or (head[1] + 1 == tail[1])
    if (not conditions_x or not conditions_y): 
        tail = prev_head_pos
        check_if_visited(tail)

# parse the direction from the line
def parse_line(line: str):
    line = line.strip("\n")
    if "R" in line:
        move("right", int(line[2:]))
    elif "U" in line:
        move("up", int(line[2:]))
    elif "L" in line:
        move("left", int(line[2:]))
    elif "D" in line:
        move("down", int(line[2:]))
    else: 
        print("shouldn't get here!")

def parse_file():
    with open("input.txt", 'r') as input_file:
        for line in input_file:
            parse_line(line)

parse_file()
print(len(grid))

"""
Notes: 
If tail needs to move we can just move into a previous head position,
so just keep that stored and use that value when needed.

Answer: 6498
"""