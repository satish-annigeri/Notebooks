from __future__ import print_function, division

import math

def linelen(x1, y1, x2=0, y2=0): # default args
    dx = x2 - x1 # x projection
    dy = y2 - y1 # y projection
    L = math.sqrt(dx**2 + dy**2) # length of line
    return L

L1 = linelen(0, 0, 3, 4)
print(L1)

L1 = linelen(0, 0, -3, -4)
print(L1)

L1 = linelen(3, 4, 0, 0)
print(L1)
