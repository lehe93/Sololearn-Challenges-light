#Das Haustier sitzt auf einem Baum fest. Mit 10 Punkten kommt es herunter. 
#Mango = 9, Lettuce = 5, Carrot: 4, Cheeseburger: 0. Input ist ein String mit allen Snacks, die wir haben. 
#Output ist "Come on Down" bei genügend Snacks oder "Time to wait", wenn zu wenige Snacks da sind.

snacks = input()

s1 = snacks.split()

points = 0

for i in s1:
    if i == "Cheeseburger":
        points += 0
    elif i == "Mango":
        points += 9
    elif i == "Carrot":
        points += 4
    elif i == "Lettuce":
        points += 5

if points >= 10:
    print("Com on Down!")
elif points < 10:
    print("Time to wait")