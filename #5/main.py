# Imports
import os
import numpy as np

### Part one ###
# Read move list and transform to suitable format
moves_raw = [line[:-1] if line[-1:]=="\n" else line for line in open(os.path.abspath("input.txt"))]
moves = [[int(r[5:].split(" from ")[0])]+list(map(int, r[5:].split(" from ")[1].split(" to "))) for r in moves_raw]

# Read stack input and transform to suitable format
stack_raw = [line[:-1] if line[-1:]=="\n" else line for line in open(os.path.abspath("input_stack.txt"))]
transform_stack = lambda stack: [stack[i+1] for i in range(0,len(stack),4)]
stack = [transform_stack(s) for s in stack_raw[:-1]]
transpose = lambda l: list(zip(*l))
piles_1 = [[c for c in p if c != " "] for p in transpose(stack)]
piles_2 = [[c for c in p if c != " "] for p in transpose(stack)]

# Printing
stackedup_piles = lambda piles: transpose(transpose(transpose([(np.max([len(p) for p in piles])-len(p))*[" "]+p for p in piles])))
printable_stack = lambda piles: "".join([" ".join([f"[{ss}]" if ss != " " else f" {ss} " for ss in s]) + "\n" for s in stackedup_piles(piles)] + [f" {i}  " for i in range(1,10)])
printable_move = lambda move: f"Move {move[0]} from {move[1]} to {move[2]}"

# Function to move a pile
cratemover9000 = lambda m, p: [p[m[1]-1].pop(0) for _ in range(m[0])][::-1] + p[m[2]-1]

# Move every pile
def heavy_lifting(piles,moves,crate_mover,plot=False):
    if plot:
        print("Starting position\n")
        print(printable_stack(piles))
    
    # Move every move, till no moves can move anymore ... move on
    for move in moves:
        piles[move[2]-1] = crate_mover(move,piles)
        if plot:
            print("\n",printable_move(move))
            print(printable_stack(piles))

    # Get result
    highest_crates = "".join([p[0] for p in piles])
    print(f"The crates at the top of all piles result in: {highest_crates}")


heavy_lifting(piles_1,moves,cratemover9000,plot=False)

### Part two ###
# Function to move a pile

cratemover9001 = lambda m, p: [p[m[1]-1].pop(0) for _ in range(m[0])] + p[m[2]-1]
heavy_lifting(piles_2,moves,cratemover9001,plot=False)