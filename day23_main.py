# Import libraries
# import numpy as np
import time

# Measure time
start = time.time()

# Define path
# data = "389125467"
data = "463528179"

# Part 1 values
# moves = 100
# lenel = 9

# Auxiliary variables
moves = 10000000
lenel = 1000000

# Data to list of elements from class elem
cups = [0] * (lenel + 1)

for i in range(1, lenel):
    if i < len(data):
        cups[int(data[i - 1])] = int(data[i])
    elif i == len(data):
        cups[int(data[i - 1])] = i + 1
    else:
        cups[i] = i + 1

# Assign from the perspective of first
cups[i + 1] = int(data[0])

# Check list validity
assert cups.count(0) == 1, "List not filled in properly"

# Set first element -- first
current = cups[i + 1]

for m in range(moves):
    # Report
    if m % 1000000 == 0:
        print(m)

    # Save values to move
    new = cups[current]
    vals = []
    for _ in range(3):
        vals.append(new)
        new = cups[new]

    # Remove elements to move list
    cups[current] = new

    # Find element to assign to
    new_val = current - 1 if current != 1 else lenel
    while new_val in vals:
        new_val = new_val - 1 if new_val != 1 else lenel

    # Move elements
    cups[new_val], cups[vals[2]] = vals[0], cups[new_val]

    # Set new current
    current = cups[current]

# Produce result
print(cups[1] * cups[cups[1]])

# Print output time
end = time.time()
print(end - start)
