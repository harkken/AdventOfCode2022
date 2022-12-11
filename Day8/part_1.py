"""
Day 8


Part 1

Transpose Matrix ftw
"""
MAX_RANGE = 99
MAX_ROW_INDEX = 98

matrix = []

transpose_matrix = [[0]*MAX_RANGE for _ in range(0, MAX_RANGE)]

# tokenize
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = list(map(int, [*line]))
        matrix.append(line)


for i in range(0,MAX_RANGE):
    for j in range(0,MAX_RANGE):
        transpose_matrix[i][j] = matrix[j][i]


def check_left(row, col, num):
    """
    vis from left
    """
    return num > max(matrix[row][:col])

def check_right(row, col, num):
    """
    vis from right
    """
    return num > max(matrix[row][col+1:])

def check_top(row, col, num):
    """
    vis from top
    """
    return num > max(transpose_matrix[col][:row])

def check_bottom(row, col, num):
    """
    vis from bottom
    """
    return num > max(transpose_matrix[col][row+1:])

def run_checks(row, col, num):
    return check_left(row, col, num) or check_right(row, col, num) or check_bottom(row, col, num) or check_top(row, col, num)


count = 0
for row in range(len(matrix)):
    for col in range(len(matrix)):
        # edges
        if row == 0 or row == MAX_ROW_INDEX or col == 0 or col == MAX_ROW_INDEX:
            count += 1
        # internals
        else:
            if run_checks(row, col, matrix[row][col]):
                count += 1

print(count)
