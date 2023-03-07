#input ist ein String mit vier Wörtern, die eine Bestellung aufweisen. 
#Output ist der gesamte Bestallbetrag: Water = 4, Coke = 5, Cheeseburger = 10, Pizza = 6, Nachos = 6
#Wird eine falsche Bestellung aufgegeben, dann wird eine Coke/5 geordert. 

order = input()
osplit = order.split()

sum = 0

for i in osplit:
    if i == "Water":
        sum += 4.0
    elif(i == "Coke"):
        sum += 5.0
    elif(i == "Cheeseburger"):
        sum += 10.0
    elif(i == "Pizza"):
        sum += 6.0
    elif( i == "Nachos"):
        sum += 6.0
    else:
        sum += 5.0

print(round(sum * 1.07, 2))





