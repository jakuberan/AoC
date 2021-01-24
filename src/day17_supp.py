# Import libraries
import numpy as np


def life_step_3D(X):
    """Game of life step using generator expressions in 3D"""
    nbrs_count = sum(
        np.roll(np.roll(np.roll(X, h, 0), i, 1), j, 2)
        for h in (-1, 0, 1)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if (h != 0 or i != 0 or j != 0)
    )
    return (nbrs_count == 3) | (X & (nbrs_count == 2))


def life_step_4D(X):
    """Game of life step using generator expressions (in 4D)"""
    nbrs_count = sum(
        np.roll(np.roll(np.roll(np.roll(X, g, 0), h, 1), i, 2), j, 3)
        for g in (-1, 0, 1)
        for h in (-1, 0, 1)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if (g != 0 or h != 0 or i != 0 or j != 0)
    )
    return (nbrs_count == 3) | (X & (nbrs_count == 2))
