#Zahlen müssen durch 12 geteilt werden (Ticketpreis)
#Erste Zahl gibt an, wie viele Punkte ich habe
#Zweite Zahl gibt an, wie teuer mein Gewinn ist (wie viele Tickets)

points = int(input())
price = int(input())

buy = points / 12

if buy >= price:
    print("Buy it!")
else:
    print("Try again")