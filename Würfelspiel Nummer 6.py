import random
import os
import time

computerWins = 0
spielerWins = 0
runde = 1
# Variablen werden festgelegt

def clear_console():
    """Clear the console screen."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')

def draw_cube():
    """Zeigt einen statischen Würfel an (einfache ASCII-Darstellung)"""
    cube = """
  +---------+  
  | o       |  
  |    o    |  
  |      o  | 
  +---------+
    """
    print(cube)
    
def main():
    clear_console()  # Konsole leeren
    draw_cube()  # Zeichne den Würfel
    draw_cube()
    draw_cube()
    time.sleep(2)  # Warte 2 Sekunden
        
print("Best of Five: ")
print("")
for i in range(5):
    print(str(runde) + "." + " Runde")
    runde = runde + 1
    computer = random.randint(1,6) #Zufällige Zahlen werden gewürfelt
    main()
    print("")
    auswahl = input("Wähle einen der Würfel mit den Zahlen 1, 2 oder 3 aus! ")
    spieler = random.randint(1,6)

    
    
    print("Spieler: " + str(spieler))
    print("Computer: " + str(computer))
    if spieler == 6: #Es wird geguckt ob es einen Extra-Wurf gibt
        while spieler == 6:
            print("Extra-Wurf bei einer 6! ")
            spieler = random. randint(1,6)
            print("Spieler: " + str(spieler))
    elif computer == 6: #Es wird geguckt ob es einen Extra-Wurf gibt
        while computer == 6:
            print("Extra-Wurf bei einer 6! ")
            computer = random. randint(1,6)
            print("Computer: " + str(computer))
        
    
    if spieler > computer: #Hier wird geguckt, wer die höhere Zahl gewürfelt hat.
        print("Spieler gewinnt! ")
        spielerWins = spielerWins + 1
        print(" ")
    elif computer > spieler:
        print("Computer gewinnt!" )
        computerWins = computerWins + 1
        print(" ")
    else:
        print("Unentschieden! ")
        print(" ")
    time.sleep(3)
        
print(" ")    
print("Der Spieler hat " + str(spielerWins) + " Runden gewonnen! ") #Es wird ausgegeben, wer wieviele Runden gewonnen hat
print("Der Computer hat " + str(computerWins) + " Runden gewonnen! ")
print("")

if spielerWins > computerWins: #Der insgesamte Gewinner wird ausgegeben
    print("Der Spieler gewinnt! ")
elif computerWins > spielerWins:
    print("Der Computer gewinnt! ")
else:
    print("Unentschieden! ")