#Ist der Hut teurer in Pesos oder in Dollar? Ausgabe sagt, welche Währung günstiger ist. 
#Umrechnungskurs: 1 Dollar = 50 Pesos / 2ct = 1 Pesos

pesos = int(input())
dollars =  int(input())

exchange = pesos * 0.02

if exchange < dollars:
    print("Pesos")
else:
    print("Dollars")