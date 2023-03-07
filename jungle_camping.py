#Ausgabe, welches Tier sich hinter den input-Geräuschen verbirgt. Grr = Lion, Rawr = Tiger, Ssss = Snake, Chirp = Bird

noise = input().split()

animals = ""

for i in noise:
    if i == "Grr":
        animals += "Lion "
    elif i == "Rawr":
        animals += "Tiger "
    elif i == "Ssss":
        animals += "Snake "
    elif i == "Chirp":
        animals += "Bird "

print(animals)



# Alternative Lösung nach input mit replace-Kombination:
# print(noise.replace("Grr", "Lion").replace("Rawr", "Tiger").replace("Ssss", "Snake").replace("Chirp", "Bird"))

 

