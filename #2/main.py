# Imports
import os
import numpy as np
PATH = os.path.abspath("input.txt")

### Part one ###
# Read
file = open(PATH)
rps = [line[:-2].split(" ") if len(line)>4 else line[:-1].split(" ") for line in file]
scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "Loss": 0,
    "Draw": 3,
    "Win": 6
}

def calc_play(play):
    convert = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }
    he = play[0]
    me = convert[play[1]]
    
    if me == he:
        return "Draw"

    #           Rock   vs  Scissors |    Paper   vs     Rock    |   Scissors   vs     Paper
    elif (me == "A" and he == "C") or (me == "B" and he == "A") or (me == "C" and he == "B"):
        return "Win"
    
    else:
        return "Loss"

scores_sign = np.sum([scores[row[1]] for row in rps])
scores_play = np.sum([scores[calc_play(row)] for row in rps])
scores_cumulated = scores_sign+scores_play
print(f"Your total score: {scores_cumulated}")

### Part two ###
def calc_play(play):
    scores = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    win = {
        "A": "B",
        "B": "C",
        "C": "A"
    }
    loss = {
        "A": "C",
        "B": "A",
        "C": "B"
    }
    he = play[0]
    me = play[1]
    score_play = scores[me]
    
    # Draw
    if me == "Y":
        score_sign = scores[he]
        
    # Win
    elif me == "Z":
        score_sign = scores[win[he]]
        
    # Loss
    else:
       score_sign = scores[loss[he]]
       
    score = score_play + score_sign
    return score
    
    
scores_cumulated = np.sum([calc_play(row) for row in rps])
print(f"Your total score: {scores_cumulated}")