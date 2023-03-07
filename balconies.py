#Erster Input sind zwei Zahlen mit Komma getrennt für die Balkon-Maße von Wohnung A, Zweiter Input für Wohnung B
#Programm soll ausgeben, welche Wohnung den größeren Balkon hat. 

flata = input()
flatb = input()

flata1 = flata.split(",")
flatb1 = flatb.split(",")

heighta = int(flata1[0])
widtha = int(flata1[1])

balkona = heighta * widtha

heightb = int(flatb1[0])
widthb =  int(flatb1[1])
balkonb = heightb * heightb 

if balkona > balkonb:
    print("Apartment A")
else:
    print("Apartment B")

