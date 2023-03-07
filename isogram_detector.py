# String als input und Ergebnis ist true oder false, wenn der Input ein Isogram ist. 
# Isogramme sind Wörter, in denen Buchstaben nur einmal vorkommen. 

word = input()

x = 0

for char in word:
    if word.count(char) > 1:
        x += 1       
 
if x == 0:
    print("true")
else:
    print("false")

