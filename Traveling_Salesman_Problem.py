import sys
from datetime import datetime
import numpy as np
from random import randrange
import matplotlib.pyplot as plt
import math



def generateArray(num):
    x, nr, xx, yy = 0, 0, 0, 0
    temp = []
    while x <= num:
        nr = x
        xx = randrange(1, 1000)
        yy = randrange(1, 1000)
        temp.append([nr, xx, yy])
        x = x + 1

    return temp


def getTime():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    dt_object = datetime.fromtimestamp(timestamp)
    print(" =", dt_object)


# test_array = [[0, 207, 217],
#               [1, 209, 300],
#               [2, 208, 216],
#               [3, 264, 262],
#               [4, 207, 220],
#               [5, 206, 133],
#               [6, 269, 451],
#               [7, 308, 226],
#               [8, 1000, 267],
#               [9, 173, 222],
#               [10, 104, 426]]

# num = int(input("How many cities? :  "))
test_array = generateArray(8)
print(test_array)
array_visited = []
x = 0
shortest_path = 0
city_nr = 0
minimum = float(sys.maxsize)
current_city = 0
temp2x = []
temp2y = []
m = 0
final_sum = 0
array_visited.append(0)
temp2x.append(test_array[0][1])
temp2y.append(test_array[0][2])
print()
getTime()
while m < len(test_array) - 1:

    while x < len(test_array):
        shortest_path = math.sqrt(
            pow((test_array[current_city][1] - test_array[x][1]), 2) + pow(
                (test_array[current_city][2] - test_array[x][2]), 2))

        if x not in set(array_visited):
            if shortest_path < minimum and shortest_path > 0:
                minimum = shortest_path
                city_nr = test_array[x][0]
                # print('city nr: '+ str(city_nr))

        x = x + 1

    x = 0
    final_sum = final_sum + minimum
    minimum = float(sys.maxsize)

    shortest_path = 0
    current_city = city_nr
    array_visited.append(current_city)

    temp2x.append(test_array[current_city][1])
    temp2y.append(test_array[current_city][2])
    m = m + 1

getTime()

print('Final sum = ' + str(final_sum))
fig, axs = plt.subplots(3)
axs[0].plot(temp2x, temp2y, 'r', zorder=2, lw=3)
axs[0].scatter(temp2x, temp2y, s=30, zorder=3)
for i, txt in enumerate(array_visited):
    axs[0].annotate(txt, (temp2x[i], temp2y[i]))

# -----------------------------------------------------------------------------brute force
def perm(a):
    if len(a) <= 1:
        yield a
    else:
        for i in range(len(a)):
            for p in perm(a[:i] + a[i + 1:]):
                yield [a[i]] + p


# test_array = generateArray(10)

startx = test_array[0][1]
starty = test_array[0][2]

array = np.arange(len(test_array))
a = array.tolist()
a.pop(0)

tracemin = float(sys.maxsize)
besttrace = []
print("brute start:")
getTime()

for p in perm(a):
    i = 0
    trace = 0
    startxnow = startx
    startynow = starty
    while i < len(p):
        trace = trace + math.sqrt(
            pow((startxnow - test_array[p[i]][1]), 2) +
            pow((startynow - test_array[p[i]][2]), 2))
        startxnow = test_array[p[i]][1]
        startynow = test_array[p[i]][2]
        i = i + 1
    if trace < tracemin:
        tracemin = trace
        besttrace = p

besttrace.insert(0, 0)

tempx = []
tempy = []
print("brute stop:")
getTime()
for j in besttrace:
    tempx.append(test_array[j][1])
    tempy.append(test_array[j][2])

m=0
trace = 0
while m < len(besttrace)-1:
    trace=trace+math.sqrt(
            pow(( test_array[besttrace[m]][1] - test_array[besttrace[m+1]][1]), 2) +
            pow(( test_array[besttrace[m]][2] - test_array[besttrace[m+1]][2]), 2))
    m=m+1

axs[1].plot(tempx, tempy, 'r', zorder=2, lw=2)
axs[1].scatter(tempx, tempy, s=50, zorder=3)
print("Final sum Brute: " + str(trace))



# -------------------------------------------------------------------------------------------------------------kruskal

m = 0
x = 0
new_array = []
print("kruskal start: ")
getTime()
while m < len(test_array):
    while x < len(test_array):
        if m != x:
            shortest_path = math.sqrt(
                pow((test_array[m][1] - test_array[x][1]), 2) + pow(
                    (test_array[m][2] - test_array[x][2]), 2))
            new_array.append([shortest_path, m, x])
        x = x + 1
    m = m + 1
    x = m
new_array.sort()
array_visited = []
for j in new_array:
    count = 0
    m = 0
    pos = 0
    while m < len(array_visited):
        if array_visited[m] == j[1] or array_visited[m] == j[2]:
            pos = m
            count = count + 1
        m = m + 1

    if count == 0:
        array_visited.append(j[1])
        array_visited.append(j[2])
    elif count == 1:
        if pos == 0:
            if j[1] == array_visited[0]:
                array_visited.insert(0, j[1])
                array_visited.insert(0, j[2])
            else:
                array_visited.insert(0, j[2])
                array_visited.insert(0, j[1])
        elif pos == len(array_visited):
            if j[1] == array_visited[len(array_visited) - 1]:
                array_visited.append(j[1])
                array_visited.append(j[2])
            else:
                array_visited.append(j[2])
                array_visited.append(j[1])
        else:
            if j[1] == array_visited[pos]:
                array_visited.insert(pos + 1, j[1])
                array_visited.insert(pos + 2, j[2])
            else:
                array_visited.insert(pos + 1, j[2])
                array_visited.insert(pos + 2, j[1])

print("kruskal stop: ")
getTime()
res = [i for n, i in enumerate(array_visited) if i not in array_visited[:n]]

tempx = []
tempy = []

m = 0

for j in res:
    tempx.append(test_array[j][1])
    tempy.append(test_array[j][2])



m = 0
trace = 0
while m < len(res) - 1:
    trace = trace + math.sqrt(
        pow((test_array[res[m]][1] - test_array[res[m + 1]][1]), 2) +
        pow((test_array[res[m]][2] - test_array[res[m + 1]][2]), 2))
    m = m + 1

print("Final sum Kruskal: " + str(trace))




axs[2].plot(tempx, tempy, 'r', zorder=2, lw=2)
axs[2].scatter(tempx, tempy, s=50, zorder=3)


plt.show()