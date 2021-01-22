# Import libraries
# import numpy as np

# Define path
# data_path = "data/day09_test"
data_path = "data/day09"

# Parameters
preamble = 25
numbers = []

f = open(data_path, "r")
for x in f:
    check = int(x.strip())

    # if we have enough numbers, start calculations
    if len(numbers) == preamble:
        temp = [check - num for num in numbers]
        if len(list(set(temp) & set(numbers))) == 0:
            print(check)
            break

        numbers.pop()
    numbers.insert(0, check)

# Part 2
f = open(data_path, "r")
numbers = [0]
for x in f:
    numbers.insert(0, int(x.strip()))
    while sum(numbers) > check:
        numbers.pop()
    if len(numbers) > 0 and sum(numbers) == check:
        num1 = min(numbers)
        num2 = max(numbers)
        print("{} + {} = {}".format(str(num1), str(num2), str(num1 + num2)))
        break
