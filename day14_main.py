# Import libraries
# import numpy as np

# Define path
# data_path = "data/day14_test"
data_path = "data/day14"

memory = {}

f = open(data_path, "r")
for x in f:
    dta = x.strip().split()
    if dta[0] == "mask":
        mask = [c for c in dta[2]]
    else:
        pos = int(dta[0].replace("mem[", "").replace("]", ""))
        val = "{0:36b}".format(int(dta[2]))
        fin = [
            "1" if (m == "1" or (m != "0" and val[i] == "1")) else "0"
            for i, m in enumerate(mask)
        ]
        memory[pos] = int("".join(fin), 2)

print("Memory sum: " + str(sum(memory.values())))
