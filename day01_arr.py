# Define path
data_path = "data/input01/input"

# Read line-by-line
list_of_sums = []
f = open(data_path, "r")
for x in f:
    # Convert to int and append
    list_of_sums.append(int(x))

# Sort
list_of_sums.sort()

# Start of count
end = len(list_of_sums) - 1
for i in range(len(list_of_sums)):
    while list_of_sums[i] + list_of_sums[end] > 2020:
        end -= 1

    if list_of_sums[i] + list_of_sums[end] == 2020:
        print("{} + {} = 2020".format(str(list_of_sums[i]), str(list_of_sums[end])))

    # Check if the list was exhausted
    if i + 1 >= end:
        break
