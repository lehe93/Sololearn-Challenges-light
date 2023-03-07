#Es gibt Popsicles für alle Geschwister, aber nur, wenn es keine Reste gibt.
#Input sind die Anzahl der Geschwister und die Popsicles, Output ist "give away", wenn keine Reste da sind
#oder "eat them yourself", wenn es Reste geben sollte. 

siblings = int(input())
popsicles = int(input())

if popsicles % siblings == 0:
    print("give away")
else:
    print("eat them yourself")