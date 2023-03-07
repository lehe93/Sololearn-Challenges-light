#Kaleidoscopes kosten 5.00 $. Steuer liegt bei 7%. Wenn Käufer mehr als eines kauft, erhält er 10% auf alle (4.9 pro Stück).

order = int(input())

if order == 1:
    print(round((order * 5 * 1.07), 2))
elif order > 1:
    print(round(((order * 5 * 0.9) * 1.07), 2))