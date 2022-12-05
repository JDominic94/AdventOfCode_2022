# Imports
import os
import numpy as np
PATH = os.path.abspath("input.txt")

### Part one ###
# Read
file = open(PATH)
calories = [int(line[:-2]) if len(line[:-2])>1 else np.nan for line in file]

# Calc where the break between elfs is, cumulate the inbetweens and check for max
calories_break_positions = np.where(np.isnan(calories))[0]
calories_cummulated = [np.sum(calories[calories_break_positions[(i-1)]+1:calories_break_positions[i]]) for i in range(1,len(calories_break_positions))] + [np.sum(calories[calories_break_positions[-1]+1:])]
calories_max = np.max(calories_cummulated)
elf_max = np.argmax(calories_cummulated)
print(f"Elf {elf_max} carried the maximum calories of {calories_max} cal")

### Part two ###
# Sort and pick the biggest three calories
calories_top_three = np.sum(np.sort(calories_cummulated)[-3:])
elf_top_three = np.argsort(calories_cummulated)[-3:]
print(f"Elfes {elf_top_three} carried the most calories with the sum of {calories_top_three} cal")
