#Newton-Raphson method to find a real root of an equation***********
from __future__ import division, print_function
import numpy as np
import math
x0=input ('enter the initial approx')
tol=input('enter the tolarence value')
n=range(100)
print("itr, x")
f= lambda x: 3*x-math.cos(x)-1
df=lambda x: 3+math.sin(x)
for i in n:
    x1=x0-(f(x0)/df(x0))
    if abs(x1-x0)>tol:
        print (i,x1)
        x0=x1
        i=i+1
    else:
        break