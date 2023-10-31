A1 = int(input("Enter A1: "))
B1 = int(input("Enter B1: "))
C1 = int(input("Enter C1: "))

A2 = int(input("Enter A2: "))
B2 = int(input("Enter B2: "))
C2 = int(input("Enter C2: "))

D = (A1*B2) - (A2*B1)
x = (C1*B2 - C2*B1)/D
y = (A1*C2 - A2*C1)/D

print(x)
print(y)