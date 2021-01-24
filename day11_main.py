# Import libraries
# import numpy as np
from src.day11_supp import is_seat, count_board, assign_fixed, count_fixed

# Define path
# data_path = "data/day11_test"
data_path = "data/day11"

# define output data
data = []

# Read line-by-line
f = open(data_path, "r")
for x in f:
    data.append([c for c in x.strip()])

# Calculate paramters
height = len(data)
width = len(data[0])

# Calulate counts
counts = count_board(data, width, height)

# Loop for seat assignment
while is_seat(data, width, height):
    counts = count_board(data, width, height)
    data = assign_fixed(data, counts, width, height)

print("Number of seats: " + str(count_fixed(data, width, height)))
