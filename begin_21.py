import math

x1 = int(input('Enter X1: '))
y1 = int(input('Enter Y1: '))
x2 = int(input('Enter X2: '))
y2 = int(input('Enter Y2: '))
x3 = int(input('Enter X3: '))
y3 = int(input('Enter Y3: '))

a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(a)
print(b)
print(c)

print("S= ", s)