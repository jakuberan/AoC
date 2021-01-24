# Import libraries
# import numpy as np
from src.day16_supp import is_valid

# Define path
# data_path = "data/day16_test2"
# data_path = "data/day16_test"
data_path = "data/day16"

# Parameter of highest number and data structure
part = 1
options = []
invalid = []
names = []

f = open(data_path, "r")
for x in f:
    x = x.strip()

    # Change part
    if x == "":
        part += 1

    # Build up the available options
    if part == 1:
        splited = x.split()
        names.append(splited[0])
        opt1 = splited[len(splited) - 1].split("-")
        opt2 = splited[len(splited) - 3].split("-")
        options.append(
            list(range(int(opt2[0]), int(opt2[1]) + 1))
            + list(range(int(opt1[0]), int(opt1[1]) + 1))
        )
    if part == 2 and not x.startswith("your") and len(x) > 0:
        own_numbers = [int(n) for n in x.split(",")]
        check_nums = []
        for i in range(len(own_numbers)):
            line = []
            for j in range(len(own_numbers)):
                line.append(1)
            check_nums.append(line)

    # Check nearby tickets
    if part == 3 and not x.startswith("nearby") and len(x) > 0:
        nums = [int(n) for n in x.split(",")]
        if is_valid(nums, options):
            for j, n in enumerate(nums):
                for i, opt in enumerate(options):
                    if n not in opt:
                        check_nums[i][j] = 0

# Adjust the field
while sum([sum(line) for line in check_nums]) > len(check_nums):
    for i, opt in enumerate(check_nums):
        if sum(opt) == 1:
            idx = opt.index(1)
            for j in range(len(check_nums)):
                if j != i:
                    check_nums[j][idx] = 0

# Solution
total = 1
keyword = "departure"
for i, name in enumerate(names):
    if name.startswith(keyword):
        idx = check_nums[i].index(1)
        total *= own_numbers[idx]

print(total)
