# Import libraries
# import numpy as np
from src.day14_supp import assign_float

# Define path
# data_path = "data/day14_test2"
# data_path = "data/day14_test"
data_path = "data/day14"

memory = {}

f = open(data_path, "r")
for x in f:
    dta = x.strip().split()
    if dta[0] == "mask":
        mask = [c for c in dta[2]]
    else:
        pos = "{0:36b}".format(int(dta[0].replace("mem[", "").replace("]", "")))
        val = int(dta[2])
        fin = "".join(
            [
                "1"
                if m == "1"
                else "X"
                if m == "X"
                else pos[i]
                if pos[i] != " "
                else "0"
                for i, m in enumerate(mask)
            ]
        )
        memory = assign_float(fin, val, memory)

print("Memory sum: " + str(sum(memory.values())))
