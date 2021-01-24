# Import libraries
# import numpy as np

# Define path
# data_path = "data/day16_test"
data_path = "data/day16"

# Parameter of highest number and data structure
part = 1
options = []
invalid = []
f = open(data_path, "r")
for x in f:
    x = x.strip()

    # Change part
    if x == "":
        part += 1

    # Build up the available options
    if part == 1:
        splited = x.split()
        opt1 = splited[len(splited) - 1].split("-")
        opt2 = splited[len(splited) - 3].split("-")
        options.append(
            list(range(int(opt2[0]), int(opt2[1]) + 1))
            + list(range(int(opt1[0]), int(opt1[1]) + 1))
        )

    # Check nearby tickets
    if part == 3 and not x.startswith("nearby") and len(x) > 0:
        nums = [int(n) for n in x.split(",")]
        for n in nums:
            check = 0
            for opt in options:
                if n in opt:
                    check = 1
                    break
            if check == 0:
                invalid.append(n)

print("Scanning error: " + str(sum(invalid)))
