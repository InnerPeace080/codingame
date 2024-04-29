import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

current_thor_position = [initial_tx, initial_ty]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(f"Thor position: {initial_tx},{initial_ty}", file=sys.stderr, flush=True)
    direction_vector = [light_x - current_thor_position[0], light_y - current_thor_position[1]]
    print(f"Direction vector: {direction_vector}", file=sys.stderr, flush=True)

    angle = math.degrees(math.atan2(direction_vector[1], direction_vector[0]))

    print("Angle: ", angle, file=sys.stderr, flush=True)

    # map angle to direction
    offset_pos = [0, 0]
    if angle > -22.5 and angle <= 22.5:
        offset_pos = [1, 0]
        print("E")
    elif angle > 22.5 and angle <= 67.5:
        offset_pos = [1, 1]
        print("SE")
    elif angle > 67.5 and angle <= 112.5:
        offset_pos = [0, 1]
        print("S")
    elif angle > 112.5 and angle <= 157.5:
        offset_pos = [-1, 1]
        print("SW")
    elif angle > 157.5 or angle <= -157.5:
        offset_pos = [-1, 0]
        print("W")
    elif angle > -157.5 and angle <= -112.5:
        offset_pos = [-1, -1]
        print("NW")
    elif angle > -112.5 and angle <= -67.5:
        offset_pos = [0, -1]
        print("N")
    elif angle > -67.5 and angle <= -22.5:
        offset_pos = [1, -1]
        print("NE")
    else:
        print("Error", file=sys.stderr, flush=True)

    current_thor_position = [a+b for a, b in zip(current_thor_position, offset_pos)]
