import sys
from random import randrange

import ax as ax
import matplotlib.pyplot as plt
import math

def generateArray(num):
    x, nr, xx, yy= 0, 0, 0, 0
    temp = []
    while x <= num:
        nr = x
        xx = randrange(1, 1000)
        yy = randrange(1, 1000)
        temp.append([nr, xx, yy])
        x = x + 1

    return temp

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
num = int(input("How many cities? :  "))
test_array=generateArray(num)
array_visited = []
x = 0
shortest_path = 0
city_nr = 0
minimum = float(sys.maxsize)
current_city = 0
temp2x = []
temp2y = []
m = 0
# nr miast
array_visited.append(0)
temp2x.append(test_array[0][1])
temp2y.append(test_array[0][2])

while m < len(test_array)-1:

    print(len(array_visited))

    while x < len(test_array):
        shortest_path = math.sqrt(
            pow((test_array[current_city][1] - test_array[x][1]), 2) + pow(
                (test_array[current_city][2] - test_array[x][2]), 2))

        if x not in set(array_visited):
            if shortest_path <= minimum and shortest_path>0:
                minimum = shortest_path
                city_nr = test_array[x][0]
                print('city nr: '+ str(city_nr))

        x = x + 1

    x = 0
    minimum = float(sys.maxsize)
    shortest_path = 0
    current_city = city_nr
    array_visited.append(current_city)
    print(array_visited)
    temp2x.append(test_array[current_city][1])
    temp2y.append(test_array[current_city][2])
    m = m + 1

print(temp2x)
print(temp2y)
plt.plot(temp2x, temp2y, 'r', zorder=2, lw=3)
plt.scatter(temp2x, temp2y, s=30, zorder=3)
for i, txt in enumerate(array_visited):
    plt.annotate(txt, (temp2x[i], temp2y[i]))
plt.show()

# wybierz miasto
# znajdz najkrótszą następną droge
