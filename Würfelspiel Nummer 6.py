import random
zahl = random.randint(1, 100)
highscore = 100

for i in range(10):
    versuch = int(input("Rate die Zahl! "))
    if versuch == zahl:
        print("Richtig geraten! ")
        highscore = str(i)
    elif versuch > zahl:
        print("Zu hoch! ")
    else:
        print("Zu niedrig! ")
