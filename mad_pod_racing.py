import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


is_boosted = False

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    print("next_checkpoint_dist=" + str(next_checkpoint_dist) + ":" + "is_boosted=" + str(is_boosted), file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    thrust = "0"
    if next_checkpoint_angle > 50 or next_checkpoint_angle < -50 or next_checkpoint_dist < 600:
        thrust = "0"
    else:
        thrust = str(math.floor(100 * min((next_checkpoint_dist - 600) / 1000, 1)))

    if (not is_boosted) and next_checkpoint_angle < 20 and next_checkpoint_angle > -20 and next_checkpoint_dist > 4500:
        is_boosted = True
        thrust = "BOOST"

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + thrust)
