#Ich will Apfelkuchen backen. Wie viele Kuchen kann ich backen?
#Es werden 3 Äpfel pro Kuchen benötigt. Input ist die Anzahl aller Äpfel und Bananen (50/50).
#Output ist Menge an Apfelkuchen, die gebacken werden kann.

fruit = int(input())

applepie = int((fruit / 2) // 3)

print(applepie)