V = int(input('Enter the speed in pool: '))
U = int(input('Enter the speed in the river: '))
T1 = int(input('Enter the time in pool: '))
T2 = int(input('Enter the time in the river: '))

S1 = T1 * V 
S2 = T2 * (V - U)
print(f' Way across the pool: {S1}')
print(f' Way across the river: {S2}')