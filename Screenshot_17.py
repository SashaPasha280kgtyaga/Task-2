import math
a = [2, 2]
b = [7, 5]

x = b[0] - a[0]
y = b[1] - a[1]

way = (math.pow(x, 2) + math.pow(y, 2)) ** 0.5
print(round(way, 3))