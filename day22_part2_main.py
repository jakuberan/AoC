# Import libraries
# import numpy as np
from src.day22_supp import play_game, eval_deck

# Define path
# data_path = "data/day22_test"
# data_path = "data/day22_test2"
data_path = "data/day22"

# Auxiliary variables
p1 = []
p2 = []
player = 1

f = open(data_path, "r")
for x in f:
    x = x.strip()
    if player == 1 and x != "" and not x.startswith("P"):
        p1.append(int(x))
    if player == 2 and x != "" and not x.startswith("P"):
        p2.append(int(x))

    # Turn player counter
    if x == "Player 2:":
        player = 2

p = play_game(p1.copy(), p2.copy())
print(eval_deck(p[1]))
