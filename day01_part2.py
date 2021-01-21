# Define path
data_path = "data/input01/input"

# Read line-by-line
list_of_sums = []
f = open(data_path, "r")
for x in f:
    # Convert to int
    x = int(x)

    # Go over the list of inputs - brute force approach
    if len(list_of_sums) > 0:
        for r in range(len(list_of_sums)):
            for l in range(r + 1, len(list_of_sums)):
                if list_of_sums[r] + list_of_sums[l] + x == 2020:
                    print(
                        "{}*{}*{} = {}".format(
                            str(x),
                            str(list_of_sums[r]),
                            str(list_of_sums[l]),
                            str(list_of_sums[r] * list_of_sums[l] * x),
                        )
                    )

    # Add the input to the list
    list_of_sums.append(x)
