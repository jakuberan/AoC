# Import libraries
# import numpy as np
from src.day24_supp import identify

# Define path
# data_path = "data/day24_test"
data_path = "data/day24"

# Auxiliary variables
tiles = []

f = open(data_path, "r")
for x in f:
    x = [c for c in x.strip()]
    tile = identify(x)
    if tile in tiles:
        tiles.remove(tile)
    else:
        tiles.append(tile)

print(len(tiles))

for step in range(100):
    # reporting
    if step % 10 == 0:
        print(step)

    # Count neighbors of black tiles
    neighbors = []
    black_cnt = {}
    new_blacks = []
    new_whites = []

    for tile in tiles:
        # Append all neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != j:
                    neighbors.append([tile[0] + i, tile[1] + j])

    # Count black tiles around
    for tile in neighbors:
        if str(tile) in black_cnt:
            black_cnt[str(tile)] += 1
        else:
            black_cnt[str(tile)] = 1

    # Apply rules on black tiles
    for tile in black_cnt.keys():
        if black_cnt[tile] == 2:
            if eval(tile) not in tiles:
                new_blacks.append(eval(tile))

    # Apply rules on white tiles
    for tile in tiles:
        if str(tile) in black_cnt.keys():
            if black_cnt[str(tile)] not in [1, 2]:
                new_whites.append(tile)
        else:
            new_whites.append(tile)

    # Update tiles
    for tile in new_whites:
        tiles.remove(tile)
    for tile in new_blacks:
        tiles.append(tile)

print(len(tiles))
