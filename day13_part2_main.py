# Import libraries
# import numpy as np
from functools import reduce

# Define path
# data_path = "data/day13_test"
data_path = "data/day13"

f = open(data_path, "r")
for i, x in enumerate(f):
    if i == 0:
        depart = int(x.strip())
    if i == 1:
        busses_raw = x.strip().split(",")

# Application of construction proof of the Chinese Remainder Theorem
# Process busses
busses = [int(b) for b in busses_raw if b != "x"]

# Save numbers
r = [(-busses_raw.index(str(b)) % b) for b in busses]

# Multiply all the divisors as M
M = reduce(lambda x, y: x * y, busses)

# Calculate a, i
a = [int(M / b) for b in busses]
j = [pow(a[i], b - 2, b) for i, b in enumerate(busses)]

# Calculate Z
Z = sum([j[i] * r[i] * a[i] for i in range(len(busses))])

# Result
print("Result: " + str(int(Z % M)))
