"""
The Elf finishes helping with the tent and sneaks back over to you. 
"Anyway, the second column says how the round needs to end: X means you need to lose,
Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
"""


score = 0


## 1 1 ROCK LOSE - SCISSORS (3)
## 1 2 ROCK DRAW - ROCK ( 1 )
## 1 3 ROCK WIN   - PAPER (2)

## PAPER LOSE - ROCK (1)
## PAPER DRAW - PAPER (2)
## PAPER WIN   - SCISSORS (3)

## SCISSORS LOSE - PAPER (2)
## SCISSORS DRAW - SCISSORS (3)
## SCISSORS WIN   - ROCK (1)
def determine_result(a, b):
    a = int(a)
    b = int(b)
    if a == 1:
        if b == 1:  # LOSE 
            return  3 +  0
        if b == 2:  # DRAW
            return  1  + 3
        if b == 3:  # WIN
            return  2 + 6
    elif a == 2:    
        if b == 1:   
            return  1 + 0 
        if b == 2:   
            return  2 + 3
        if b == 3:    
            return  3 + 6
    elif a == 3:
        if b == 1:  
            return 2 + 0
        if b == 2:    
            return 3 + 3
        if b == 3:   
            return 1 + 6


with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().replace("A", "1").replace("B", "2").replace("C", "3").replace("X", "1").replace("Y", "2").replace("Z", "3")
        line = line.split(" ")
        score += determine_result(*line)
    print(score)