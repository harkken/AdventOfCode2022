"""
Day 8


Part 2

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

def find_max_in_list(li, val):
    test_li = []
    for item in li:
        test_li.append(item)
        if val <= max(test_li):
            return len(test_li)
    return len(li)

def scenic_left(row, col, num):
    """
    vis from left
    """
    return find_max_in_list(list(reversed(matrix[row][:col])), num)

def scenic_right(row, col, num):
    """
    vis from right
    """
    return find_max_in_list(matrix[row][col+1:], num)

def scenic_top(row, col, num):
    """
    vis from top
    """
    return find_max_in_list(list(reversed(transpose_matrix[col][:row])), num)

def scenic_bottom(row, col, num):
    """
    vis from bottom
    """
    return find_max_in_list(transpose_matrix[col][row+1:], num)

def run_checks(row, col, num):
    return scenic_left(row, col, num) * scenic_right(row, col, num) * scenic_top(row, col, num) * scenic_bottom(row, col, num)



scenic_score = 0
count = 0
for row in range(len(matrix)):
    for col in range(len(matrix)):
        # edges
        if row == 0 or row == MAX_ROW_INDEX or col == 0 or col == MAX_ROW_INDEX:
            count += 1
        # internals
        else:
            t = run_checks(row, col, matrix[row][col])
            # update scenic score
            if t > scenic_score:
                scenic_score = t
                
print(scenic_score)
