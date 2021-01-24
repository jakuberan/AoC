# Import libraries
# import numpy as np

# Define path
# data_path = "data/day22_test"
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

# Play the game
while len(p1) * len(p2) > 0:
    p1n = p1.pop(0)
    p2n = p2.pop(0)
    if p1n > p2n:
        p1.append(p1n)
        p1.append(p2n)
    else:
        p2.append(p2n)
        p2.append(p1n)

# Winning array
if len(p1) > 0:
    p = p1
else:
    p = p2

# Evaluate the result
out = 0
for i in range(len(p)):
    out += p[i] * (len(p) - i)

print(out)
