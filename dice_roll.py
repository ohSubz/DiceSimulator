# Funktionen für Haupttool.
# Import der Random Bib.
import random
# Dice Simulation 

def ddice(dice_number):
    dice_typs = [4,6,8,10,12,20,100]
    d_n = []
    dice_range = dice_number + 1
    # a correct dice was selected
    if dice_number in dice_typs:
        if dice_number == 100:
            print("Accepted cube")
        else:
            d_n = []
            print(d_n.extend(range(1,dice_range)))      #Erstellen einer zweiten Liste mit der Range 1-Würfel Zahl
            d_n = random.sample(d_n,1)
    else:
        print("So a cube does not exist!")
    
    return d_n[0]                                       #Ausgabe der gewürfelten Zahl

print(ddice(12))