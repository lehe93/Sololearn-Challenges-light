#Polizist in Gotham. Soll Batman gerufen werden oder nicht
#Wenn Verbrecher-Input unter 5, dann "I got this!"; Input == 5 bis 10, dann "Help me Batman"
#Input > 10, dann "Good Luck out there!"

i = int(input())

if i < 5:
    print("I got this!")
elif i == 5 and i <= 10: 
    print("Help me Batman")
elif i > 10:
    print("Good Luck out there!")