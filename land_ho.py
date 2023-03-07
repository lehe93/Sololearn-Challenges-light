#Großes Schiff hält vor einem schönen Strand und alle Gäste wollen mit kleinem Boot hinfahren.
#Kleines Boot kann 20 Personen mitnehmen und braucht 10 Minuten für jede Strecke (Hin oder Zurück)
#Input ist die Position in Warteschlange, Output ist die Zeit, bis man am Strand ist. 

p = int(input())

print(int(int(p / 20) * 20 + 10))
