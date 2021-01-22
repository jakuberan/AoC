# Define path
# data_path = "data/day02_test"
data_path = "data/day02"

# Read line-by-line
list_of_sums = []
valid = 0
f = open(data_path, "r")
for x in f:
    x_in = x.split(" ")

    # save intevals
    [low, high] = x_in[0].split("-")
    letter = x_in[1][0]

    # Check validity
    if (x_in[2][int(low) - 1] == letter) != (x_in[2][int(high) - 1] == letter):
        valid += 1

print(str(valid))
