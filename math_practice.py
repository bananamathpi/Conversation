# Abraham, 9/9/19
# Math practice problems
# Sources: None
# OMH

from math import sin, cos, sqrt
import sys

# Problem 1
G = int(input('Input a value for G: '))
mass1 = int(input('Input a value for the first mass:'))
mass2 = int(input('Input a value for the second mass:'))
radius = int(input('Input a value for the radius:'))

force = G * mass1 * mass2 / radius * radius
# The problem here is that the student did not take into account order of operations.
print('This is the wrong value:', force)

force = G * mass1 * mass2 / (radius * radius)
# This fixes the problem by adding parentheses, which are done first.
print('This is the correct value:', force)

force = G * mass1 * mass2 / radius ** 2
# Similarly, this replaces the multiplation with an exponent, which is done before the other operations.
print('This is the correct value:', force)

# Problem 2
# import math
# import sys

print('\nValue for theta: ', sys.argv[1])
theta = int(sys.argv[1])

sin = math.sin(theta)
cos = math.cos(theta)

print('sin(Ø)^2 + cos(Ø)^2 =', sin ** 2 + cos ** 2)
# Might not always be 1.0 because of rounding.

# Problem 3
# import math

x = int(input('\nInput x coordinate: '))
y = int(input('Input y coordinate: '))

distance = math.sqrt(x ** 2 + y ** 2)
print('Distance from origin =', distance)

