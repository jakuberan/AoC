# Import libraries
# import numpy as np
from src.day18_supp import evaluate

# Define path
# data_path = "data/day18_test"
data_path = "data/day18"

# Obtain the dimension
total = 0
f = open(data_path, "r")
for x in f:
    x = [c for c in x.strip() if c != " "]
    out = evaluate(x)
    total += out[1]

print("Sum of all results: " + str(total))
