a = int(input('Corner a: '))

while a < 0 or a > 2 * 3.14:
	print('a must be betwin 0 and 6.28')
	a = int(input('Corner a: '))

result = a * 180 / 3.14
print(result)
