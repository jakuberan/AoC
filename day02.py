# Define path
# data_path = "data/input02/input_test"
data_path = "data/input02/input"

# Read line-by-line
list_of_sums = []
valid = 0
f = open(data_path, "r")
for x in f:
    x_in = x.split(" ")

    # save intevals
    [low, high] = x_in[0].split("-")
    count = x_in[2].count(x_in[1][0])

    # Check validity
    if int(low) <= count and count <= int(high):
        valid += 1

print(str(valid))
