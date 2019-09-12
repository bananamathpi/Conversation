# Abraham, 9/10/19
# Advanced math practice
# Sources: None
# OMH

import math
import sys

# Problem 1
t = float(sys.argv[1])
v = float(sys.argv[2])

w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
print(w)

# Problem 2
x = float(sys.argv[3])
y = float(sys.argv[4])
z = float(sys.argv[5])

print(x < y < z or x > y > z)

# Problem 3
m = int(sys.argv[6])
d = int(sys.argv[7])
y = int(sys.argv[8])

y0 = (y - math.floor((14 - m)/12))
x = y0 + math.floor(y0/4) - math.floor(y0/100) + math.floor(y0/400)
m0 = m + 12 * math.floor((14 - m)/12) - 2
d0 = (d + x + math.floor((31 * m0)/12)) % 7

print(d0)