# Import libraries
# import numpy as np
from src.day12_supp import rotate

# Define path
# data_path = "data/day12_test"
data_path = "data/day12"

# Memory variables
posx = 0
posy = 0
wpx = 10
wpy = 1

f = open(data_path, "r")
for x in f:
    # print(x)
    act = x.strip()[0]
    num = int(x.strip()[1:])

    # Rotations
    if act in ["L", "R"]:
        if act == "R":
            num = -num
        wpx, wpy = rotate(wpx, wpy, num)

    # Applying cardinal directions
    if act in ["E", "W"]:
        if act == "W":
            num = -num
        wpx += num
    if act in ["S", "N"]:
        if act == "S":
            num = -num
        wpy += num

    # Moving forward
    if act == "F":
        posx += num * wpx
        posy += num * wpy

print("Total distance: " + str(int(abs(posy) + abs(posx))))
