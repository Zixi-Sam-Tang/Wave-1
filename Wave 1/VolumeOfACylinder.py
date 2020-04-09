import math
radius = int(input())
height = int(input())
vol = radius ** 2 * math.pi * height
print("{:.1f}".format(vol))