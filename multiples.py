# Summe aller Multiplen von 3 und 5 unter einer angegebenen Nummer (Input).

x = int(input())

y = 0
sum = 0

while y < x:    
    if y%3==0 or y%5 == 0:
        sum += y
    y += 1

print(sum)

