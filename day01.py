# Define path
data_path = "data/input01/input"

# Read line-by-line
list_of_sums = []
f = open(data_path, "r")
for x in f:
    # Convert to int
    x = int(x)
    
    # Go over the list of inputs
    if len(list_of_sums) > 0:
        for r in list_of_sums:
            if r + x == 2020:
                print("{}*{} = {}".format(str(x), str(r), str(r*x)))
    
    # Add the input to the list
    list_of_sums.append(x)
