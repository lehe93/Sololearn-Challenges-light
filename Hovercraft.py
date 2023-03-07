#Firma baut Hovercrafts für 2000000 pro Stück und verkauft sie für 3000000.
#Pro Monat muss 1000000 an Versicherung gezahlt werden. 
#Input ist die Menge an Verkäufen und Output ist "Broke Even", "Profit" oder "Loss"

orders = int(input())

c = 2
i = 1
s = 3
b = 10

costs = b * c + i
sales = s * orders

if costs == sales:
    print("Broke Even")
elif costs < sales: 
    print("Profit")
elif costs > sales:
    print("Loss")

