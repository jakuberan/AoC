# Import libraries
# import numpy as np
from src.day21_supp import update_allergens

# Define path
# data_path = "data/day21_test"
data_path = "data/day21"

# Auxiliary variables
allergens_all = {}
ingreds_all = []
allergens = {}

f = open(data_path, "r")
for x in f:
    allergs = []
    dta = x.strip().split("(")

    # Derive ingredients and allergens
    ingreds = [i.strip() for i in dta[0].split()]
    allergs = dta[1].replace("contains ", "").replace(")", "").replace(",", "")
    allergs = [i.strip() for i in allergs.split()]

    # Update overall ingredients list
    ingreds_all = list(set(ingreds) | set(ingreds_all))

    # Update allergens list
    for allerg in allergs:
        if allerg in allergens_all.keys():
            allergens_all[allerg] = list(set(allergens_all[allerg]) & set(ingreds))
        else:
            allergens_all[allerg] = ingreds
        # If the list became a single list, update this and all previous allergens
        update_allergens(allerg, allergens, allergens_all)

# Get the list of fixed ingredients
ingreds_fixed = []
for allerg in allergens.keys():
    for ingr in allergens[allerg]:
        ingreds_fixed.append(ingr)

appearances = 0
f = open(data_path, "r")
for x in f:
    dta = x.strip().split("(")
    appearances += sum([1 for i in dta[0].split() if i.strip() not in ingreds_fixed])

print("Total appearances of ok ingredients: " + str(appearances))

# Canonical dangerous ingredient list
out = ""
allergs = list(allergens.keys())
allergs.sort()
for allg in allergs:
    out += allergens[allg][0] + ","

print(out[: (len(out) - 1)])
