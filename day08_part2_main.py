# Import libraries
# import numpy as np

# Define path
# data_path = "data/day08_test"
data_path = "data/day08"

# Build graph structure
program = []

f = open(data_path, "r")
for x in f:
    op = x.strip().split()
    program.append([op[0], int(op[1])])

# run the program
changes = {"nop": "jmp", "jmp": "nop"}
for i in range(len(program) - 1, -1, -1):
    if program[i][0] in ["nop", "jmp"]:
        program[i][0] = changes[program[i][0]]

        # Run the changed program
        head = 0
        state = 0
        used = []
        while head not in used and head < len(program):
            used.append(head)
            if program[head][0] == "acc":
                state += program[head][1]
                head += 1
            elif program[head][0] == "nop":
                head += 1
            elif program[head][0] == "jmp":
                head += program[head][1]

        # Change back if needed
        if head == len(program):
            print(state)
            break
        program[i][0] = changes[program[i][0]]
