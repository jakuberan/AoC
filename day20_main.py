# Import libraries
# import numpy as np
from math import sqrt
from src.day20_supp import (
    gen_borders,
    flip,
    rotate,
    is_matching,
    cbind,
    is_monster,
    match_right,
)

# Define path
# data_path = "data/day20_test"
data_path = "data/day20"

# Auxiliary variables
dim = 10

f = open(data_path, "r")
tilnum = []
tiles = []
borders = {}
read = 0
for x in f:
    if read > 0:
        if read == dim:
            tile = []
        tile.append([c for c in x.strip()])
        read -= 1
        if read == 0:
            tiles.append(tile)
            border = gen_borders(tile) + gen_borders(flip(tile))
            num = tilnum[len(tilnum) - 1]
            for b in list(set(border)):
                if b in borders.keys():
                    borders[b].append(num)
                else:
                    borders[b] = [num]
    if x.strip().startswith("Tile"):
        tilnum.append(int(x.strip().split()[1].replace(":", "")))
        read = dim

# Create a dictionary of neighbors
neig_dct = {}
for num in tilnum:
    neig_dct[num] = []

# Create a list of pairs
pair_dct = {}
pairs = []
for b in borders.keys():
    if b[::-1] in borders.keys():
        for p1 in borders[b]:
            for p2 in borders[b[::-1]]:
                if p1 != p2:
                    pairs.append([p1, p2])
                    neig_dct[p1].append(p2)
                    neig_dct[p2].append(p1)
                    for p in [p1, p2]:
                        if p in pair_dct.keys():
                            pair_dct[p] += 1
                        else:
                            pair_dct[p] = 1

# Normalize dictionary
output = 1
for p in pair_dct.keys():
    pair_dct[p] = int(pair_dct[p] / 4)
    if pair_dct[p] == 2:
        output *= p
        corner = p

print(output)

# Adjust neighbors dictionary
for num in tilnum:
    neig_dct[num] = list(set(neig_dct[num]))

# Create the complete image -- with boundaries included
match_num = corner
tilenumbers = [corner]
tile = (tiles[tilnum.index(tilenumbers[0])]).copy()
output = []
dim_tile = len(tile)
max_dim = int(sqrt(len(tilnum)))

# Rotate until fits
for i in range(max_dim):

    # Append new line to output
    for _ in range(len(tile)):
        output.append([])

    # Match on a single line
    for j in range(max_dim):
        to_rotate = False
        while not is_matching(tile, [match_num], i, j, output, max_dim, borders):
            if to_rotate:
                tile = flip(tile)
                tile = rotate(tile)
                to_rotate = False
            else:
                tile = flip(tile)
                to_rotate = True

        # Add rotated tile to the end
        output = cbind(output, tile)

        # Select next tile
        if i < max_dim - 1 or j < max_dim - 1:
            if j < max_dim - 1:
                match_num = borders[match_right(tile)]
                match_num = list(set(match_num) - set(tilenumbers))[0]
            else:
                above_neig = neig_dct[tilenumbers[len(tilenumbers) - max_dim]]
                other_neig = [tilenumbers[len(tilenumbers) - max_dim + 1]]
                if len(tilenumbers) >= 2 * max_dim:
                    other_neig.append(tilenumbers[len(tilenumbers) - 2 * max_dim])
                match_num = list(set(above_neig) - set(other_neig))[0]
            tilenumbers.append(match_num)
            tile = (tiles[tilnum.index(match_num)]).copy()

# Adjust image
output_final = []
for i in range(len(output)):
    line = []
    for j in range(len(output)):
        if j % 10 not in [0, 9]:
            line.append(output[i][j])
    if i % 10 not in [0, 9]:
        output_final.append(line)


# Search for monster
monsters = 0
to_rotate = False
while monsters == 0:
    # Check monsters
    for i in range(1, len(output_final) - 1):
        for j in range(0, len(output_final) - 19):
            monsters += is_monster(output_final, i, j)

    # Rotate / Flip
    if to_rotate:
        output_final = flip(output_final)
        output_final = rotate(output_final)
        to_rotate = False
    else:
        output_final = flip(output_final)
        to_rotate = True

# Calculate water elements
water = sum(
    [
        1
        for i in range(len(output_final))
        for j in range(len(output_final))
        if output_final[i][j] == "#"
    ]
)

# Water less monsters
print("Roughness: " + str(water - monsters * 15))
