def identify(moves):
    """
    Identify tile according to moves
    """
    idx = 0
    idy = 0
    i = 0
    while i < len(moves):
        if moves[i] in ["e", "w"]:
            mult = 1
            if moves[i] == "e":
                mult = -1
            idx += 1 * mult
            idy += -1 * mult
        else:
            if moves[i] == "s":
                if moves[i + 1] == "e":
                    idy += 1
                else:
                    idx += 1
            else:
                if moves[i + 1] == "e":
                    idx += -1
                else:
                    idy += -1
            i += 1
        i += 1

    # Return identified tile
    return [idx, idy]
