def assign_float(mem, value, memory):
    """
    Function for memory retrieval
    """
    if mem.count("X") == 0:
        memory[int(mem, 2)] = value
        return memory
    else:
        x = mem.index("X")
        memory = assign_float(mem[:x] + "0" + mem[(x + 1) :], value, memory)
        memory = assign_float(mem[:x] + "1" + mem[(x + 1) :], value, memory)

    return memory
