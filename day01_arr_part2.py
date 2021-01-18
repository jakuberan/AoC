# Define path
data_path = "data/input01/input"
target = 2020

# Read line-by-line
list_of_sums = []
f = open(data_path, "r")
for x in f:
    # Convert to int and append
    list_of_sums.append(int(x))

# sort    
list_of_sums.sort()

# start of count
for i in range(len(list_of_sums) - 2):
    
    # check if the sum has not become too large
    if list_of_sums[i] + list_of_sums[i + 1] + list_of_sums[i + 2] > target:
        break
    
    part_target = target - list_of_sums[i]
    
    # Inner loop of narrowing interval
    mid = i + 1
    end = len(list_of_sums) - 1
    
    while mid < end:
        mid_val = list_of_sums[mid]
        end_val = list_of_sums[end]
        
        # We need to narrow from above
        if mid_val + end_val > part_target:
            end -= 1
        elif mid_val + end_val < part_target:
            mid += 1
        else:
            print("{} * {} * {} = {}".format(
                str(list_of_sums[i]),
                str(mid_val),
                str(end_val),
                str(list_of_sums[i]*mid_val*end_val)))
            break
