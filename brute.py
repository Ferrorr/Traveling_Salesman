import sys
from random import randrange
import matplotlib.pyplot as plt
import math
import numpy as np

def perm(a):
    if len(a) <= 1:
        yield a
    else:
        for i in range(len(a)):
            for p in perm(a[:i]+a[i+1:]):
                yield [a[i]]+p



test_array = [[0, 207, 217],
              [1, 209, 300],
              [2, 208, 216],
              [3, 264, 262],
              [4, 207, 220],
              [5, 206, 133],
              [6, 269, 451],
              [7, 308, 226],
              [8, 1000, 267],
              [9, 173, 222],
              [10, 104, 426]]

startx=test_array[0][1]
starty=test_array[0][2]

array=np.arange(len(test_array))
a = array.tolist()
a.pop(0)

tracemin=float(sys.maxsize)
besttrace=[]

for p in perm(a):
    i=0
    trace=0
    startxnow=startx
    startynow=starty
    while i < len(p):
        trace=trace+math.sqrt(
            pow((startxnow - test_array[p[i]][1]), 2) +
            pow((startynow - test_array[p[i]][2]), 2))
        startxnow=test_array[p[i]][1]
        startynow=test_array[p[i]][2]
        i=i+1
    if trace < tracemin:
        tracemin=trace
        besttrace = p
besttrace.insert(0,0)


tempx = []
tempy = []

for j in besttrace:
    tempx.append(test_array[j][1])
    tempy.append(test_array[j][2])

plt.plot(tempx, tempy, 'r', zorder=2, lw=2)
plt.scatter(tempx, tempy, s=50, zorder=3)
plt.show()