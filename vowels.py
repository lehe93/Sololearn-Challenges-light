#input ist ein string und Programm soll vokale/vowels zählen und ausgeben

word = input()

count = 0 
vowels = "aeiouAEIOU"

for i in word:
    if i in vowels:
        count += 1

print(count)