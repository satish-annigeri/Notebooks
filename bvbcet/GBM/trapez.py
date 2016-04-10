#Trapezoidal rule for integration********
from __future__ import division, print_function
import numpy as np
import math

a,b=input ("enter the lower and upper limits")
n=input("enter the no of divisions")
h=(b-a)/n
f= lambda x: 1.0/(1+x*x)
s=f(a)+f(b)
k=range(a,b,h)
print("ans=",s)