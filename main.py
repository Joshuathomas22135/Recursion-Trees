""" A Python program that uses recursive branching to count all possible paths through a grid when movement is allowed only to the
right or down, showing how the recursion tree grows quickly."""

def pathsThroughGrid(x, y):
    if x == 1 or y == 1:
        return 1
    return pathsThroughGrid(x - 1, y) + pathsThroughGrid(x, y - 1)