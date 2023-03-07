#Farbe kosten 5 pro Stück, Leinand/Canvas kostet 40 und Steuern sind 10 %. 
#Output sind die gesamten Kosten gerundet. 

colors = int(input())
canvas = 40
tax = 1.1

total = ((colors * 5) + canvas) * tax

print(round(total))