#Beim Halloween-Abend werden Snacks etc. eingesammelt. Auch Dollarnoten werden verteilt. 
#2 Häuser geben immer Dollarnoten ab, ein Haus gibt Zahnbürsten ab. Der Rest verteilt Snacks.
#Wie hoch ist die Wahrscheinlichkeit eine Dollarnote aus dem eigenen Beutel zu ziehen? 

houses = int(input())

x = (2 / houses) * 100

prozent = int(x)

if prozent != x:
    print(int(x+1))
else:
    print(int(x))