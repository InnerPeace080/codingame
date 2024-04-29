import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

boundary = [0, w, 0, h]

floor_or_ceil = math.ceil


def get_new_position(x, y, direction):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_
        direction (_type_): can be U D L R
    """
    global floor_or_ceil

    if floor_or_ceil == math.floor:  # type: ignore
        floor_or_ceil = math.ceil
    elif floor_or_ceil == math.ceil:  # type: ignore
        floor_or_ceil = math.floor

    if direction == "U":
        boundary[3] = y
        return x, floor_or_ceil((y + boundary[2]) / 2)
    elif direction == "D":
        boundary[2] = y
        return x, floor_or_ceil((y + boundary[3])/2)
    elif direction == "L":
        boundary[1] = x
        return floor_or_ceil((x + boundary[0])/2), y
    elif direction == "R":
        boundary[0] = x
        return floor_or_ceil((x + boundary[1])/2), y

    return x, y


current_pos_x = x0
current_pos_y = y0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # split char of bomb_dir
    bomb_dir = list(bomb_dir)
    for direction in bomb_dir:
        current_pos_x, current_pos_y = get_new_position(current_pos_x, current_pos_y, direction)

    # the location of the next window Batman should jump to.
    print(f"{current_pos_x} {current_pos_y}")
