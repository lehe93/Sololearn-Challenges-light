#Der Input ist ein Text und der Output soll das längste Wort aus dem Text sein. 

txt = input()

#your code goes here

text = txt.split(" ")

print(max(text, key=len))

# Mit der Funktion max kann eine liste nach dem Element mit dem höchsten Wert durchsucht werden.
# Das Attribut key = len gibt den Wert an, welcher als höchstes angesehen wird. In diesem Fall ist es die Zeichenlänge. 
