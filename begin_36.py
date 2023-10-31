V1 = int(input("Enter speed 1: "))
V2 = int(input("Enter speed 2: "))
S = int(input("Destination betwin 1 and 2: "))
T = int(input("Vremya "))

S1 = V1 * T
S2 = V2 * T

print("All way", S1 + S2 + S)
print("All way v2", ((V1+V2)*T)+S)