# Import libraries
# import numpy as np

# Define path
# data_path = "data/day13_test"
data_path = "data/day13"

f = open(data_path, "r")
for i, x in enumerate(f):
    if i == 0:
        depart = int(x.strip())
    if i == 1:
        busses_raw = x.strip().split(",")

# Process busses
busses = [int(b) for b in busses_raw if b != "x"]
delay = depart
for b in busses:
    if b - depart % b < delay:
        delay = b - depart % b
        bus = b

print("Bus {}, delay {}: {}".format(str(bus), str(delay), str(bus * delay)))
