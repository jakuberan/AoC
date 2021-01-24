def flip(m):
    """
    Flips a tile
    """
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def gen_borders(tile, dim=10):
    """
    Generates all borders of a tile
    """
    return [
        "".join(tile[0]),
        "".join(tile[dim - 1][::-1]),
        "".join([tile[i][dim - 1] for i in range(dim)]),
        "".join([tile[i][0] for i in range(dim - 1, -1, -1)]),
    ]


def rotate(m):
    """
    Rotates a tile
    """
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]


def cbind(m1, m2):
    """
    Column binds two tiles
    """
    out = []
    for i in range(len(m1) - len(m2)):
        out.append(m1[i])
    for i in range(len(m2)):
        out.append(m1[len(m1) - len(m2) + i] + m2[i])
    return out


def match_up(m):
    """
    Returns border to match from above
    """
    return "".join(m[0])


def match_down(m):
    """
    Returns border to match from below
    """
    return "".join(m[len(m) - 1])


def match_right(m):
    """
    Returns border to match from right
    """
    return "".join([m[i][len(m) - 1] for i in range(len(m) - 1, -1, -1)])


def match_left(m):
    """
    Returns border to match from left
    """
    return "".join([m[i][0] for i in range(len(m))])


def is_matching(m, m_num, i, j, out, max_dim, borders):
    """
    Checks if a tile is matching to partially completed picture
    """
    matches = 0
    if i != 0:
        up_border = "".join(out[i * len(m) - 1][(j * len(m)) : ((j + 1) * len(m))])
        matches += match_up(m) == up_border
    else:
        matches += 1
    if j != 0:
        left_border = "".join(
            [out[i][j * len(m) - 1] for i in range(len(out) - len(m), len(out))]
        )
        matches += match_left(m) == left_border
    else:
        matches += 1
    if i != max_dim - 1:
        m_down = match_down(m)
        if m_down in borders.keys():
            if len(set(borders[m_down]) - set(m_num)) > 0:
                matches += 1
    else:
        matches += 1
    if j != max_dim - 1:
        m_right = match_right(m)
        if m_right in borders.keys():
            if len(set(borders[m_right]) - set(m_num)) > 0:
                matches += 1
    else:
        matches += 1

    return matches == 4


def is_monster(img, i, j):
    """
    Searches for a monster at a specific position
    """
    if img[i][j] == ".":
        return 0
    if img[i + 1][j + 1] == ".":
        return 0
    if img[i + 1][j + 4] == ".":
        return 0
    if img[i][j + 5] == ".":
        return 0
    if img[i][j + 6] == ".":
        return 0
    if img[i + 1][j + 7] == ".":
        return 0
    if img[i + 1][j + 10] == ".":
        return 0
    if img[i][j + 11] == ".":
        return 0
    if img[i][j + 12] == ".":
        return 0
    if img[i + 1][j + 13] == ".":
        return 0
    if img[i + 1][j + 16] == ".":
        return 0
    if img[i][j + 17] == ".":
        return 0
    if img[i][j + 18] == ".":
        return 0
    if img[i - 1][j + 18] == ".":
        return 0
    if img[i][j + 19] == ".":
        return 0

    return 1
