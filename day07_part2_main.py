# Import libraries
# import numpy as np
from src.day07_supp import process_rule_part2, total_bags_from_color

# Define path
# data_path = "data/day07_test2"
# data_path = "data/day07_test"
data_path = "data/day07"

# save output graph
graph = {}

# Build graph structure
f = open(data_path, "r")
for x in f:
    graph = process_rule_part2(graph, x.strip())

# Get total number of bags needed
print(total_bags_from_color(graph, "shiny_gold") - 1)
