import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

nearest20 = None

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    if nearest20 is None or abs(t) < abs(nearest20) or (abs(t) == abs(nearest20) and t > nearest20):
        nearest20 = t

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if nearest20 is None:
    nearest20 = 0

print(str(nearest20))
