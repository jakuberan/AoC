# Import libraries
# import numpy as np

# Define path
# data_path = "data/day15_test"
data_path = "data/day15"

# Parameter of highest number and data structure
up_to = 30000000
said = {}

f = open(data_path, "r")
for x in f:
    # Save input array to dictionary
    arr = x.strip().split(",")
    last = int(arr[-1])
    for i, a in enumerate(arr[: (len(arr) - 1)]):
        said[int(a)] = i

    # Play the game
    for i in range(len(arr), up_to):
        if last in said.keys():
            temp = i - 1 - said[last]
            said[last] = i - 1
            last = temp
        else:
            said[last] = i - 1
            last = 0

print("The {} number spoken is {}".format(str(up_to), str(last)))
