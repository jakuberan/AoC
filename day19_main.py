# Import libraries
# import numpy as np
from src.day19_supp import get_messages, validate8

# Define path
# data_path = "data/day19_test2"
# data_path = "data/day19_test"
data_path = "data/day19"

# Obtain the dimension
rules_raw = {}
rules_fin = {}
messages = []
part = 1

f = open(data_path, "r")
for x in f:
    # Save input information
    if x.strip() == "":
        part = 2
    elif part == 1:
        rule = x.strip().split(":")
        rule_content = rule[1].strip().replace('"', "")
        if rule_content in ["a", "b"]:
            rules_fin[int(rule[0])] = [rule_content]
        else:
            rules_raw[int(rule[0])] = rule_content
        # Save rule if final
    else:
        messages.append(x.strip())

# Build up the rulebase
valid8 = get_messages(8, rules_raw, rules_fin)
valid31 = get_messages(31, rules_raw, rules_fin)
valid42 = get_messages(42, rules_raw, rules_fin)

# Enumerate messages
len8 = len(valid8[0])
len31 = len(valid31[0])
len42 = len(valid42[0])

# Apply the final set of rules with loops
valids = {"8": valid8, "31": valid31, "42": valid42}
lens = {"8": len8, "31": len31, "42": len42}
valid_messages = [m for m in messages if validate8(m, 0, len(m), lens, valids)]
print("There are {} messages obeying the rules".format(str(len(valid_messages))))
