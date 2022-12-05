# Imports
import os
import numpy as np
PATH = os.path.abspath("input.txt")

### Part one ###
# Init
lower_dict = {chr(i+96): i for i in range(1,27)}
upper_dict = {chr(i+65): i+27 for i in range(26)}
priority = dict(lower_dict, **upper_dict)

# Read and transform to 2D list of backpacks with transformed priority
file = open(PATH)
transform = lambda line: [priority[c] for c in line]
split = lambda line: [line[:int(len(line)/2)], line[int(len(line)/2):]]
backpacks = [split(transform(line[:-1])) if line[-1:]=="\n" else split(transform(line)) for line in file]

# Check for matching items in both compartiments in a backpack and sum up priorities
get_match = lambda backpack: [c for c in backpack[0] if c in backpack[1]][0]
score = np.sum([get_match(backpack) for backpack in backpacks])
print(f"Your priority score is: {score}")

### Part two ###
backpacks = [b[0]+b[1] for b in backpacks]
get_match = lambda backpack: [c for c in backpack[0] if (c in backpack[1]) and (c in backpack[2])][0]
score = np.sum([get_match(backpacks[i:(i+3)]) for i in range(0,len(backpacks),3)])
print(f"Your priority score is: {score}")

