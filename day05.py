# Import libraries
# import numpy as np
from src.day05_seat_to_num import seat_to_num

# Define path
data_path = "data/input05/input"

# Auxiliary parameters
max_so_far = 0

f = open(data_path, "r")
for x in f:
    max_so_far = max(max_so_far, seat_to_num(x.strip()))

print("Highest seat ID is {}".format(str(max_so_far)))

# Eliminate seats in the list
to_eliminate = list(range(max_so_far + 1))
f = open(data_path, "r")
for x in f:
    to_eliminate.remove(seat_to_num(x.strip()))

# Eliminate numbers in front and in the back
for i in range(len(to_eliminate) - 1):
    if to_eliminate[i] + 1 != to_eliminate[i + 1]:
        print(to_eliminate[i + 1])
