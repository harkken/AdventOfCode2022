"""
Advent of Code
2022 - Day 9 - Rope Bridge - PART 2!!!

"""
X = 0
Y = 1
DOWN = -1   # 0, -1 - down (neg)
UP = 1      # 0, 1  - up (pos)
LEFT = -1   # -1, 0 - left  (neg)
RIGHT = 1   # 1, 0  - right (pos)


# init 9 variable positions
start_position = [0,0]
"""
head  = [0,0] 
pos_1 = [0,0] 
pos_2  = [0,0] 
pos_3  = [0,0]
pos_4  = [0,0]
pos_5  = [0,0]
pos_6  = [0,0]
pos_7  = [0,0]
pos_8  = [0,0]
#pos_9 = 

H , 1-9, 10 total segments
"""
segments = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]] # 9
head = [0,0]
cur_segment = head
tail = segments[8]

# holds the positions visited by the tail
grid = [start_position]

def move_head(num_steps, axis, direction):
    global head   
    for _ in range(num_steps):
        head[axis] += direction
        #from ipdb import set_trace; set_trace();
        update_segments()

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


def movement_in_some_direction(seg_1, seg_2):
    """
    Need to know which direction to move in
    .....
    ....H
    .....
    ...S.
    options: left, right, up, down
             NW, NE, SW, SE
    
    Need to check 2 spots away and move into that spot
    """

    if seg_2[0] + 2 == seg_1[0]:
        seg_2[0] += 1
        #print("right")
    elif seg_2[0] - 2 == seg_1[0]:
        seg_2[0] -= 1
        #print("left")
    elif seg_2[1] + 2 == seg_1[1]:
        seg_2[1] += 1
        #print("up")
    elif seg_2[1] - 2 == seg_1[1]:
        seg_2[1] -= 1
        #print("down")
    elif seg_2[0] - 1 == seg_1[0] and seg_2[1] + 2 == seg_1[1]:
        seg_2[0] -= 1
        seg_2[1] += 1
        #print("move NW")
    elif seg_2[0] + 1 == seg_1[0] and seg_2[1] + 2 == seg_1[1]:
        seg_2[0] += 1
        seg_2[1] += 1    
        #print("move_segment_NE")
    elif seg_2[0] - 2 == seg_1[0] and seg_2[1] - 1 == seg_1[1]:
        seg_2[0] -= 1
        seg_2[1] -= 1   
        #print("move_segment_SW")    
    elif seg_2[0] + 2 == seg_1[0] and seg_2[1] - 1 == seg_1[1]:
        seg_2[0] += 1
        seg_2[1] -= 1   
        #print("move_segment_SE")  
    else:
        pass
        #print("dont_move")
    

def update_segment(segment):
    global cur_segment
    # check against cur_pos which is the node to update against
    # move segment if needed and store in segments
    # update cur_pos to be current segment which was just proceesesed

    movement_in_some_direction(cur_segment, segment)
    cur_segment = segment

    
def update_segments():
    # go through the list and update the segment if needed
    # check the first segment and update it 
    global tail, cur_segment

    for segment in segments:
        update_segment(segment)
    cur_segment = head
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
    with open("sample.txt", 'r') as input_file:
        for line in input_file:
            parse_line(line)

parse_file()
print(len(grid))

"""
Notes: 
Similar to the first half of the puzzle, but now we have 9 segments.
When the head moves, we need to go down the rope line and check if each segment relative to 
the segment in front of it.

New plan: have to move each piece and cant just move into the old location
"""