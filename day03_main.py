# Import libraries
import numpy as np

# Define path
# data_path = "data/day03_test"
data_path = "data/day03"

# define output data
data = []

# Read line-by-line
f = open(data_path, "r")
for x in f:
    data.append([c for c in x.strip()])

# Save dimensisons
length = len(data)
width = len(data[0])
trees_m = 1

# set possible moves
steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
# steps = [[3, 1]]

for step in steps:

    # Set slope moves
    w_step = step[0]
    l_step = step[1]

    # simple solution using a loop
    tree_char = "#"
    trees = 0
    w = 0
    for i in range(int(np.floor(length / l_step))):
        # Get l position
        l = i * l_step

        # count character
        if data[l][w] == tree_char:
            trees += 1

        # Modify width
        w += w_step
        if w >= width:
            w -= width

    trees_m *= trees

# Print output
print("Result: {}".format(str(trees_m)))
