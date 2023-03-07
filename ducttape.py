#eine Tür soll mit ducttape umhüllt werden. Wie viele Rollen werden gebraucht. 
#eine Rolle Ducttape umfasst 60ft Länge, 2inches Breite (1ft = 12inch)
#Input sind zwei Integers für Höhe und Breite, Output ist die gesamte Rolle an ducttape

import math
h = int(input())
w = int(input())

door_area = h * w * 2 

ducttape = 60 * (2/12)

need = math.ceil(door_area / ducttape)

print(need)