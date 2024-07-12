import math
import sys

# Save the Planet.
# Use less Fossil Fuel.

n = int(input())  # the number of points used to draw the surface of Mars.

prev_x = None
prev_y = None

surface: list[list[int]] = []

flat_surface: list[list[int]]

for i in range(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.append([land_x, land_y])

    if prev_x is not None and prev_y is not None:
        if prev_y == land_y:
            flat_surface = [[prev_x, prev_y], [land_x, land_y]]

    prev_x, prev_y = land_x, land_y

print(f"flat_surface: {flat_surface}", file=sys.stderr, flush=True)

# game loop
while True:
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # R P. R is the desired rotation angle. P is the desired thrust power.
    print("-20 3")
