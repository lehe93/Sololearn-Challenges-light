# Zipcodes können nur Nummern enthalten und müssen geprüft werden, ob sie korrekt sind. 
# Input ist ein String und soll geprüft werden, ob dieser valid ("true") oder nicht ("false") ist. 

zip = input()

char = "abcdefghijklmnopqrstuvwxyz"
count = 0

for i in zip:
    if i == " ":
        count += 1 
    elif i in char:
        count += 1
    elif len(zip) > 5 or len(zip) < 5:
        count += 1

if count > 0:
    print("false")
else:
    print("true")
