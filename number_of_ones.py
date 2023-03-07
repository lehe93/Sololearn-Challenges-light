# Eine Zahl kommt als input und nun sollen die Anzahl an 1 für die binomische Variante des Inputs gezählt werden. 

x = int(input())

y = str(bin(x))
z = 0

for i in y:
    if i == "1":
        z += 1

print(z)