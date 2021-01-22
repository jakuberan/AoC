# Import libraries
# import numpy as np

# Define path
# data_path = "data/day10_test2"
# data_path = "data/day10_test"
data_path = "data/day10"

adp = [0]
f = open(data_path, "r")
for x in f:
    adp.append(int(x.strip()))

adp.append(max(adp) + 3)

# Sort and find out the highest adapter
adp.sort()
out = [adp[i + 1] - adp[i] for i in range(len(adp) - 1)]

c3 = 0
c1 = 0
# Find and remove from larger than 3
for i in range(len(out)):
    if out[i] == 1:
        c1 += 1
    elif out[i] == 3:
        c3 += 1
    elif out[i] > 3:
        break

print("Result: {}".format(str(c1 * c3)))
