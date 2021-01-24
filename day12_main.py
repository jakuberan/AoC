# Import libraries
# import numpy as np
# from math import sin, cos

# Define path
# data_path = "data/day12_test"
data_path = "data/day12"

# Memory variables
posx = 0
posy = 0
deg = 90

f = open(data_path, "r")
for x in f:
    # print(x)
    act = x.strip()[0]
    num = int(x.strip()[1:])

    # Rotations
    if act in ["L", "R"]:
        if act == "L":
            num = -num
        deg += num
        deg = deg % 360

    # Applying cardinal directions
    if act in ["E", "W"]:
        if act == "W":
            num = -num
        posx += num
    if act in ["S", "N"]:
        if act == "S":
            num = -num
        posy += num

    # Moving forward
    if act == "F":
        if deg == 0:
            posy += num
        # elif deg < 90:
        #    posx += num * sin(deg)
        #    posy += num * cos(deg)
        elif deg == 90:
            posx += num
        # elif deg < 180:
        #    posy -= num * sin(deg - 90)
        #    posx += num * cos(deg - 90)
        elif deg == 180:
            posy -= num
        # elif deg < 270:
        #    posx -= num * sin(deg - 180)
        #    posy -= num * cos(deg - 180)
        elif deg == 270:
            posx -= num
        # elif deg < 360:
        #    posy += num * sin(deg - 270)
        #    posx -= num * cos(deg - 270)
        else:
            print("Turn not allowed!")

print("Total distance: " + str(abs(posy) + abs(posx)))
