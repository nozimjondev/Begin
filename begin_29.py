a = int(input('Corner a: '))

while a < 0 or a > 360:
	print('a must be betwin 0 and 360')
	a = int(input('Corner a: '))

result = a * 3.14 / 180
print(result)

	