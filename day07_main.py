# Import libraries
# import numpy as np
from src.day07_supp import process_rule, accessible_vertices

# Define path
# data_path = "data/day07_test"
data_path = "data/day07"

# save output graph
graph = {}

# Build graph structure
f = open(data_path, "r")
for x in f:
    graph = process_rule(graph, x.strip())

# find all accessible vertices from shiny_gold
print(len(accessible_vertices(graph, "shiny_gold")))
