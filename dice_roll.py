# Funktionen für Haupttool.

import random                                       #Import der Random Bib.

# Dice Simulation 

def ddice(dice_number):                             #Definieren der Funktion
    dice_typs = [4,6,8,10,12,20,100]                #Liste mit der Anzahl der Seiten der Würfel
    d_n = []                                        #Leere Liste
    dice_range = dice_number + 1                    #Würfel Range geht von 1-gewählten Würfel
                                                    #+1 da Python bei 0 anfängt zu zählen

    if dice_number in dice_typs:                    
        d_n.extend(range(1,dice_range))             #Erstellen einer zweiten Liste mit der Range 1-Würfel Zahl
        d_n = random.sample(d_n,1)                  #Zufällige auswahl der Zahl
    else:
        print("So a cube does not exist!")
    
    return d_n[0]                                   #Ausgabe der gewürfelten Zahl

print(ddice(100))                                   #Auswahl des Würfels