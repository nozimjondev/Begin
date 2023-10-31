import math

x1 = int(input('Enter X1: '))
x2 = int(input('Enter X2: '))
y1 = int(input('Enter Y1: '))
y2 = int(input('Enter Y2: '))

length = abs(x2 - x1)
height = abs(y2 - y1)
print(f'Length: {length}, Height: {height}')

p = (length + height) * 2
s = length * height
print(f'P= {p}, S= {s}') 