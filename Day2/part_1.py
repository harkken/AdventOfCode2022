"""
Day 2 - Part 1 

Rock Paper Scissors
"""


'''
A = Rock     = X  = 1
B = Paper    = Y  = 2
C = Scissors = Z  = 3

0 = lose
3 = draw
6 = win
'''


'''
paper beats rock    B > A | 2 > 1|  lose
scissors beat paper C > B | 3 > 2|  lose
rock beats scissors A > C | 1 > 3|  lose

rock 1
paper 2
scissors 3

1 2 win
3 1 win
2 3 win

1 3 lose
2 1 lose
3 2 lose
'''
score = 0

def determine_result(a, b):
    a = int(a)
    b = int(b)
    if a == b: # draw
        return 3 + b
    if (a > b and a == 3 and b == 1): # rock beats scissors - win
        return 6 + b
    if (b > a and b == 3 and a == 1): # rock beats scissors - lose
        return 0 + b 
    if b > a : #  win
        return 6 + b
    return 0 + b  # lose
        

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().replace("A", "1").replace("B", "2").replace("C", "3").replace("X", "1").replace("Y", "2").replace("Z", "3")
        line = line.split(" ")
        score += determine_result(*line)
    print(score)
