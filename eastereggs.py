#Es ist Zeit für eine Ostereiersuche mit einem Freund. 3 Inputs: erster Input ist gesamte Menge an Eiern
#Zweiter Input sind Eier in meinem Korb, dritter Input sind Eier im Korb des Freundes. 
#Output ist "Candy Time", wenn alle Eier gefunden wurden, ansonsten "Keep Hunting"

total = int(input())
me = int(input())
him = int(input())

if total == (me + him):
    print("Candy Time")
else:
    print("Keep Hunting")