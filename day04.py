# Import libraries
# import numpy as np
from src.day04_passport import Passport

# Define path
# data_path = "data/input04/input_invalid"
# data_path = "data/input04/input_valid"
# data_path = "data/input04/input_test"
data_path = "data/input04/input"

# Read line-by-line
valid = 0
document = Passport()

f = open(data_path, "r")
for x in f:
    if x == "\n":
        valid += document.validate()
        print("Document {} is {}".format(document.get_string(), document.validate()))
        document = Passport()
    else:
        document.add_data(x)

# validate last passport
valid += document.validate()

# Print the result
print("\nThere are {} valid passports".format(str(valid)))
