#In Neverland wird niemand älter. Man geht mit seinem Zwilling hin, aber Zwilling geht irgendwann zurück. 
#Input sind das eigene Alter und das Alter des Zwillings. Output ist der folgende Satz:
#"My twin is XX years old and they are YY years older than me"

y = int(input())
s = int(input())

print("My twin is " + str(y+s) + " years old and they are " + str(s) + " years older than me")