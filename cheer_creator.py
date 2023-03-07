#Je nach Yard-Input soll ein bestimmter Ausruf erfolgen:
#über 10 Yards = "High Five", 1 - 10 Yards = Ra! für jeden Yard, <1 = "shh"

yards = int(input())

if yards >= 1 and yards <= 10:
    print("Ra!" * yards)
elif(yards > 10):
    print("High Five")
elif(yards <= 0):
    print("shh")