import math

x1 = int(input('Enter X1: '))
x2 = int(input('Enter X2: '))
y1 = int(input('Enter Y1: '))
y2 = int(input('Enter Y2: '))

r = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(r)