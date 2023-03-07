#Das Haustier sitzt auf einem Baum fest. Mit 10 Punkten kommt es herunter. 
#Mango = 9, Lettuce = 5, Carrot: 4, Cheeseeburger : 0. Input ist ein String mit allen Snacks, die wir haben. 
#Output ist "Come on Down" bei genügend Snacks oder "Time to wait", wenn zu wenige Snacks da sind.

snacks = {"Mango": 9, "Lettuce": 5, "Carrot": 4}
points = 0
inv = input().split()

for x in inv:
	points += int(snacks.get(x, 0))
if points >= 10:
	print("Come on Down!")
else:
	print("Time to wait")