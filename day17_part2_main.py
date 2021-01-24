# Import libraries
import numpy as np
from src.day17_supp import life_step_4D

# Define path
# data_path = "data/day17_test"
data_path = "data/day17"

# Auxiliary parameters
steps = 6

# Obtain the dimension
f = open(data_path, "r")
for x in f:
    x = x.strip()
    dim = len(x)
    break

# Assign auxiliary field
dim_short = 2 * steps + 1
dim_long = 2 * steps + dim
X = np.zeros((dim_short, dim_short, dim_long, dim_long), dtype=bool)

# Populate the data structure
f = open(data_path, "r")
i = steps
for x in f:
    for j, c in enumerate(x.strip()):
        if c == "#":
            X[steps, steps, i, j + steps] = True
    i += 1

# Run
for i in range(steps):
    X = life_step_4D(X)

print(sum(sum(sum(sum(X)))))
