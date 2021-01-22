# Import libraries
# import numpy as np
import string

# Define path
# data_path = "data/day06_test"
data_path = "data/day06"

# Auxiliary dictionaries
group = {k: 0 for k in string.ascii_lowercase}
total = 0
members = 0
part = 2  # Defines problem part

f = open(data_path, "r")
for x in f:
    if x == "\n":
        if part == 2:
            total += sum([k == members for k in group.values()])
        if part == 1:
            total += sum([k > 0 for k in group.values()])
        group = {k: 0 for k in string.ascii_lowercase}
        members = 0
    else:
        members += 1
        for ans in x.strip():
            group[ans] += 1

# Update last and print
if part == 2:
    total += sum([k == members for k in group.values()])
if part == 1:
    total += sum([k > 0 for k in group.values()])
print("Total sum: {}".format(str(total)))
