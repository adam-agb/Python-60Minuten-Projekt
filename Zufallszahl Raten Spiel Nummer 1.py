import random
spieler = random.randint(1, 6)
computer = random.randint(1,6)
print("Spieler: " + str(spieler))
print("Computer: " + str(computer))
if spieler == 6:
    while spieler == 6:
        print("Extra-Wurf bei einer 6! ")
        spieler = random. randint(1,6)
        print("Spieler: " + str(spieler))
elif computer == 6:
    while computer == 6:
        print("Extra-Wurf bei einer 6! ")
        computer = random. randint(1,6)
        print("Computer: " + str(computer))
    
    
if spieler > computer:
    print("Spieler gewinnt! ")
elif computer > spieler:
    print("Computer gewinnt!" )
else:
    print("Unentschieden! ")

