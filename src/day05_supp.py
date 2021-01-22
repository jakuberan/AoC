def seat_to_num(seat):
    """
    Helper function for seat to number conversion
    """
    row = int(seat[0:7].replace("B", "1").replace("F", "0"), 2)
    col = int(seat[7:10].replace("R", "1").replace("L", "0"), 2)
    # print("{}, {}".format(row, col))

    return row * 8 + col
