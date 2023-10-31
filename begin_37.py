V1 = int(input("Enter speed 1: "))
V2 = int(input("Enter speed 2: "))
S = int(input("Destination betwin 1 and 2: "))
T = int(input("Time "))

print("All way ", abs(S - ((V1+V2)*T)))