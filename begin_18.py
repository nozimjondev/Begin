import math 

A = int(input('Enter A: '))
B = int(input('Enter B: '))
C = int(input('Enter C: '))

while C <= A  or C >= B:
	print('C must be betwin A and B')
	A = int(input('Enter A: '))
	B = int(input('Enter B: '))
	C = int(input('Enter C: '))

AC = abs(C - A)
BC = abs(C - B) 
P = AC * BC
print(P)



	