"""
Rules:
If the head is ever two steps directly up, down, left, or right from the tail,
the tail must also move one step in that direction so it remains close enough:


Otherwise, if the head and tail aren't touching and aren't in the same row or column,
the tail always moves one step diagonally to keep up:
"""

segments = [[0, 0]] * 10
visited = [[0, 0]]


DOWN = [0, -1]
UP = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]
NW = [-1, 1]
NE = [1, 1]
SW = [-1, -1]
SE = [1, -1]

all_directions = [DOWN, UP, LEFT, RIGHT, NW, NE, SW, SE]

diagonal = [NW, NE, SE, SW]


# maps input str to 2D coords
directions = {"U": UP, "D": DOWN, "L": LEFT, "R": RIGHT}


def parse_file():
    """
    Main function
    """
    with open("test.txt", "r", encoding="utf-8") as input_file:
        for line in input_file:
            parse_line(line)


def parse_line(line: str):
    """
    Parse line and move in direction
    """
    line = line.split()
    direction, steps = [line[0], int(line[1])]
    move(direction, steps)


def move(direction: str, steps: int):
    """
    Move in direction for steps
    """
    for _ in range(steps):
        move_segments(direction)


def move_segments(compass: str):
    """
    Move head and body segments by looping through the segments
    """
    direction = directions[compass]
    for i, _ in enumerate(segments):
        if i == 0:
            # head is unique in that it only responds to 4 directions
            move_head(segments, direction)
        else:
            move_body(i, direction)


def move_body(i, direction):
    """
    Move body segments
    """
    # we need the previous piece to determine which type of move it is
    current_segment = segments[i]
    previous_segment = segments[i - 1]
    move_in_direction(current_segment, previous_segment, direction, i)


def move_in_direction(current_segment, previous_segment, direction, index):
    """
    Determine which direction to move the body segments.
    Can be diagonal.
    Sometimes there is no move if they are overlapping
    or already adjacent
    """
    if (
        is_adjacent(current_segment, previous_segment)
        or current_segment == previous_segment
    ):
        return
    if is_row(current_segment, previous_segment):
        segments[index] = [sum(x) for x in zip(current_segment, direction)]
    elif is_column(current_segment, previous_segment):
        segments[index] = [sum(x) for x in zip(current_segment, direction)]
    else:
        # we know its diagonal
        diagonal_move_adjacent(segments, current_segment, previous_segment, index)

    if segments[index] not in visited and index == 9:
        print(segments[index])
        visited.append(segments[index])


def is_adjacent(current_segment, previous_segment):
    # If adjacent there is no move
    """
    o o o
    o x o
    o o o
    . . .
    """
    for direction in all_directions:
        new_list = list(map(lambda x, y: x - y, current_segment, previous_segment))
        if new_list == direction:
            return True
    return False


def is_row(current_segment, previous_segment):
    """
    . . .
    x . x
    . . .
    . . .
    """
    return current_segment[0] == previous_segment[0]


def is_column(current_segment, previous_segment):
    """
    . . .
    x . .
    . . .
    x . .
    """
    return current_segment[1] == previous_segment[1]


def diagonal_move_adjacent(segment_list, current_segment, previous_segment, index):
    """
    When we know we need a diagonal move, only one of those moves will move it into an adjacent spot
    to the previous segment. Therefore we can calculate which adjacent move will put that segment next
    to it and select that one.

    . . .
    . P .
    . . .
    C . .
    """
    # make adjacency_list for the previous segment
    adjacency_list = []
    for direction in all_directions:
        adjacency_list.append([sum(x) for x in zip(previous_segment, direction)])

    # find out which diagonal move will get the current adjacent to the previous
    for direction in diagonal:
        if [sum(x) for x in zip(current_segment, direction)] in adjacency_list:
            segment_list[index] = [sum(x) for x in zip(current_segment, direction)]
            break


def move_head(segment_list, direction: list):
    """
    Move the head in one of 4 directions:
    N, S, W, E
    """
    segment_list[0] = [sum(x) for x in zip(segment_list[0], direction)]


if __name__ == "__main__":
    parse_file()
    # from ipdb import set_trace; set_trace();
    print(len(visited))
