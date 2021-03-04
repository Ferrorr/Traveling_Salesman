from random import randrange
import matplotlib.pyplot as plt

test_array = [[1, 207, 217],
              [2, 363, 327],
              [3, 264, 262],
              [4, 371, 242],
              [5, 206, 133],
              [6, 269, 451],
              [7, 308, 226],
              [8, 74, 267],
              [9, 173, 222],
              [10, 104, 426]]


def generateArray(num):
    x, nr, xx, yy = 1, 0, 0, 0
    temp = []
    while x <= num:
        nr = x
        xx = randrange(50, 500)
        yy = randrange(50, 500)
        temp.append([nr, xx, yy])
        x = x + 1

    return temp


# tablica tablic w formacie [ nr_miasta, x, y ]
city = [0, 0, 0]
num = int(input("How many cities? :  "))
array = generateArray(num)
for arr in array:
    print(arr)
m = 0
n = 0
# koordynaty  pierwszego miasta
current_position_x = array[0][1]
current_position_y = array[0][2]
sumx = current_position_x
sumy = current_position_y
array_visited = [0]
temp2x = []
temp2y = []

temp2x.append(current_position_x)
temp2y.append(current_position_y)

array_visited.append(0)

while m < num:

    while True:
        temp = randrange(1, num)
        print(len(array_visited))
        if temp not in array_visited or len(array_visited) == num:
            break

    # todo: sprawdzić chyba błąd
    array_visited.append(temp)

    current_position_x = array[temp][1]
    temp2x.append(current_position_x)
    sumx = sumx + current_position_x

    current_position_y = array[temp][2]
    temp2y.append(current_position_y)
    sumy = sumy + current_position_y

    print(current_position_x)
    m = m + 1

plt.plot(temp2x, temp2y, 'r', zorder=2, lw=2)
plt.scatter(temp2x, temp2y, s=50, zorder=3)
plt.show()

# 1 losuj miasto początkowe
# 2 losuj miasto docelowe
# 3 jeżeli miasto zostało odwiedzone goto #2
# 4 dodaj koszty x i y
# 5 jesli brak miast break
# 6 goto 2
