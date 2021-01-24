def count_seats(board, pi, pj, w, h):
    """
    Calculates number of empty seats around a given seat
    """
    count = 0
    for i in range(max(pi - 1, 0), min(pi + 2, h)):
        for j in range(max(pj - 1, 0), min(pj + 2, w)):
            if board[i][j] == "L":
                count += 1
    return count - 1


def check_fixed(board, pi, pj, w, h):
    """
    Checks if there is a fixed seats around a given seat
    """
    for i in range(max(pi - 1, 0), min(pi + 2, h)):
        for j in range(max(pj - 1, 0), min(pj + 2, w)):
            if i != pi or j != pj:
                if board[i][j] == "#":
                    return True
    return False


def count_board(board, w, h, part=1):
    """
    Calculates for all seats on the board
    """
    out = []
    line = []
    for i in range(h):
        for j in range(w):
            if board[i][j] in [".", "#"]:
                line.append(-1)
            else:
                if part == 1:
                    line.append(count_seats(board, i, j, w, h))
                else:
                    line.append(count_seats_part2(board, i, j, w, h))
        out.append(line)
        line = []
    return out


def is_seat(board, w, h):
    """
    Checks if there is an empty seat on the board
    """
    for i in range(h):
        for j in range(w):
            if board[i][j] == "L":
                return True
    return False


def count_fixed(board, w, h):
    """
    Checks the number of fixed seats on the board
    """
    count = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == "#":
                count += 1
    return count


def assign_fixed(board, counts, w, h, lim=4, part=1):
    """
    Assigns fixed seats on the board
    """
    for i in range(h):
        for j in range(w):
            if board[i][j] == "L" and counts[i][j] < lim:
                board[i][j] = "#"
    for i in range(h):
        for j in range(w):
            if board[i][j] == "L":
                if part == 1:
                    if check_fixed(board, i, j, w, h):
                        board[i][j] = "."
                if part == 2:
                    if check_fixed_part2(board, i, j, w, h):
                        board[i][j] = "LE"
    return board


def search_in_direction(board, pi, pj, wi, wj, w, h, obj="L", block=["LE"]):
    """
    Searches for a specified seat in all directions
    """
    pi += wi
    pj += wj
    while pi < h and pi >= 0 and pj < w and pj >= 0:
        if board[pi][pj] in block:
            return 0
        if board[pi][pj] == obj:
            return 1
        pi += wi
        pj += wj
    return 0


def count_seats_part2(board, pi, pj, w, h):
    """
    Calculates number of empty seats around a given seat (for part 2)
    """
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                count += search_in_direction(board, pi, pj, i, j, w, h)
    return count


def check_fixed_part2(board, pi, pj, w, h):
    """
    Checks if there is a fixed seats around a given seat (for part 2)
    """
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if search_in_direction(
                    board, pi, pj, i, j, w, h, obj="#", block=["L", "LE"]
                ):
                    return True
    return False
