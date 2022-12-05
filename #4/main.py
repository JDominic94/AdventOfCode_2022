# Imports
import os
import numpy as np
PATH = os.path.abspath("input.txt")

### Part one ###
# Read and transform to pairs ot integer
file = open(PATH)
raw = [line[:-1] if line[-1:]=="\n" else line for line in file]
assignment_pairs = [[list(map(int, s.split("-"))) for s in r.split(",")] for r in raw]

# Check for full overlap
is_in = lambda p1,p2: p1[0]>=p2[0] and p1[1]<=p2[1]
overlap = lambda p1, p2: is_in(p1,p2) or is_in(p2,p1)
total_overlaps = np.sum([overlap(pair[0], pair[1]) for pair in assignment_pairs])
print(f"Overlaps: {total_overlaps}")



### Part two ###
# Check partly overlap
is_in = lambda p1,p2: p1[1]>=p2[0] and p1[0]<=p2[1]
overlap = lambda p1, p2: is_in(p1,p2) or is_in(p2,p1)
partial_overlaps = np.sum([overlap(pair[0], pair[1]) for pair in assignment_pairs])
print(f"Overlaps: {partial_overlaps}")